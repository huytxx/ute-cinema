$(document).ready(function() {
  

    $('.btn-chi-tiet').on('click', function() {
        console.log(this.id);
        $(location).attr('href', './chi-tiet');
    })
})
