/* Simple Simple */
$(document).ready(function(){
    /* main function */
    $("#print_em").click(function(){
        window.print();
    });
    $("#clear_em").click(function(){
        $.get("./_clear", function(data, status) {
            $("#stamped").text("Cleared.").fadeIn().fadeOut(6000);
            location.reload();
        });
    });
});