$(document).ready(function(){
    $('li a').click(function(){
        $('li a').removeClass("active");
        $(this).addClass("active");
    });
});