$(document).ready(function() {
    var info = localStorage.getItem('info_main')
    var imageSrc= localStorage.getItem('imageSrc')
    var descriptionTicket = localStorage.getItem('description')
    $("#info_ticket").html(info)
    //$("#info_ticket:first").removeClass('d-none')
    $('#imageTicket').attr('src', imageSrc)
    $('#descriptionTicket').html(descriptionTicket)
    console.log( $("#info_ticket:first").html());
})
