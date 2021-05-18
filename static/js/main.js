$(document).ready(function() {
  

    $('.btn-chi-tiet').on('click', function(event) {
        event.preventDefault();
       var str = $(this).attr('class')
        var res = str.split(" ");
        var des = $(this).find('#desTicket').text();
    //     console.log(res[0])
    //     var info_main = '.info_main_'+res[0];
    //     console.log(info_main);
    //     console.log($(`.info_main/`));
         
        //$(location).attr('href', './chi-tiet');
        $(this).first().removeClass('d-none')
       localStorage.setItem('info_main', $(this).find('.info_main').html())
       localStorage.setItem('imageSrc', res[0])
       localStorage.setItem('description', des)
       $(location).attr('href', './chi-tiet');
    })
})
