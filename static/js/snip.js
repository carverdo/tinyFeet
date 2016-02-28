/* Simple Simple */
$(document).ready(function(){
    /* some pretty boxes */
    $("input, textarea").focus(function(){
        $(this).css("background-color", "#cccccc");
    });
    $("input, textarea").blur(function(){
        $(this).css("background-color", "#ffffff");
    });
    /* main function */
    $("#print_em").click(function(){
        /* PASS OUR FORM */
        $.post("./_stamp", $("form").serialize(), function(data, status) {
            var res = data;
        });
        window.print();
    });
});