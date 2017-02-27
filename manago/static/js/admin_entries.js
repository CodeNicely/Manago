
$( "#clientform_click" ).on( "click", function() {
  $('#developerform').hide();
  $('#clientform').toggle();
});

$( "#developerform_click" ).on( "click", function() {
  $('#clientform').hide();
  $('#developerform').toggle();
});

