$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/newsecure/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $("#id_DepositorName").val('')
    $("#id_ReceiverName").val('')
    $("#id_TrackNo").val('')
    $("#id_Origin").val('')
    $("#id_Destination").val('')
    $("#id_TypeOfShipment").val('')
    $("#id_NatureOfGoods").val('')
    $("#id_Status").val('')
  }) // End of submit event

}) // End of document ready function
