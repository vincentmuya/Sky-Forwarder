$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/newcargo/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $('#id_SenderName').val('')
    $("#id_SenderAddress").val('')
    $("#id_RecieverName").val('')
    $("#id_RecieverAddress").val('')
    $("#id_referenceID").val('')
    $("#id_GoodsareFrom").val('')
    $("#id_GoodsTo").val('')
    $("#id_DepatureDate").val('')
    $("#id_Depaturetime").val('')
    $("#id_ArrivalDate").val('')
    $("#id_ArrivalTime").val('')
    $("#id_GoodsDescription").val('')
    $("#id_Status").val('')
  }) // End of submit event

}) // End of document ready function
