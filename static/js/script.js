$(document).ready(function() {
    $("#p1").click(function(){
        $(".pp1").toggle(1000);
        $("#p1").hide(1000);
       
    });
    $(".pp1").click(function(){
        $("#p1").toggle(1000);
        $(".pp1").hide(1000);

    });

})