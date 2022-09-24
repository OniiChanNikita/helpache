$(document).ready(function() {
    var p = $(".element_home_1");
    var d = $(".element_home_2");
    var r = $("#resize");
    
    var curr_width = p.width()
    var unlock = false;
    
    $(document).mousemove(function(e) {
          var change = curr_width + (e.clientX - curr_width);
        
       if(unlock) {
                if(change > 199) {
                    $("#debug").text(e.clientX + " resize");
                    p.css("width", change);
                    d.css("margin-left", change);
                }
                else {
                    p.css("width", 200);
                    d.css("margin-left", 200);
            }
        }
    });
    
    r.mousedown(function(e) {
        curr_width = p.width();
        unlock = true;
        r.css("background-color", "rgba(0, 0, 0, 0.2)");
    });

    $(document).mousedown(function(e) {
        if(unlock) {
          e.preventDefault();
        }
    });

    $(document).mouseup(function(e) {
        unlock = false;
        $("#debug").text("");
        r.css("background-color", "rgba(0, 0, 0, 0.1)");
    });
});