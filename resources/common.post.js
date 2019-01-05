$('#divStatus').click(() => {
  window.location = '/status/';
});
$('#btnToggleNav').click( () => {
  $('#topMenu .item').toggle(0);
})

$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;