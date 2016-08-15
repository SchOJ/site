import hashlib
import json
import logging
import urllib2
from contextlib import closing
from urllib import urlencode

from django.conf import settings

from judge.utils.file_cache import HashFileCache

logger = logging.getLogger('judge.texoid')

TEXOID_ENABLED = hasattr(settings, 'TEXOID_URL')


class TexoidRenderer(object):
    def __init__(self):
        self.cache = HashFileCache(settings.TEXOID_CACHE_ROOT,
                                   settings.TEXOID_CACHE_URL,
                                   getattr(settings, 'TEXOID_GZIP', False))

    def query_texoid(self, formula, hash):
        self.cache.create(hash)

        try:
            request = urllib2.urlopen(settings.TEXOID_URL, urlencode({
                'q': formula
            }))
        except urllib2.HTTPError as e:
            if e.code == 400:
                logger.error('Texoid failed to render: %s\n%s', formula, e.read())
            else:
                logger.exception('Failed to connect to texoid for: %s' % formula)
            return
        except Exception:
            logger.exception('Failed to connect to texoid for: %s' % formula)
            return

        with closing(request) as f:
            data = f.read()
            try:
                data = json.loads(data)
            except ValueError:
                logger.exception('Invalid texoid response for: %s\n%s', formula, data)
                return

        if not data['success']:
            logger.error('Texoid failure for: %s\n%s', formula, data)
            return {'error': data['error']}

        result = {
            'png': self.cache.cache_data(hash, 'png', data['png'].decode('base64')),
            'svg': self.cache.cache_data(hash, 'svg', data['svg'].encode('utf-8')),
        }
        return result

    def query_cache(self, hash):
        result = {
            'svg': self.cache.get_url(hash, 'svg'),
            'png': self.cache.get_url(hash, 'png'),
        }
        return result

    def get_result(self, formula):
        hash = hashlib.sha1(formula).hexdigest()

        if self.cache.has_file(hash, 'svg'):
            return self.query_cache(hash)
        else:
            return self.query_texoid(formula, hash)
