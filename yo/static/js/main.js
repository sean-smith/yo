    $(document).ready(function() {
        /*
	$.get("/subscriber_count", function(data){
            console.log(data)
            $("#subscribers").html("<h3 class=\"text-center\">"+data+" Subscribers</h3>");
        });
	*/
        $("#yo_form").on("submit", function(event){
            event.preventDefault();
            $("#yo_form").hide();
            username = $("#username").val();
            name = $("#name").val();
            message = $("#message").val();
            $.ajax({
                url: "/yo_message",
                type: "POST",
                data: {
                    "message": message,
                    "username": username,
                    "name": name
                },
                success: function(data){
                    $("#success").html("<h3 class=\"text-center\">"+data+"</h3>");
                }
            });
            return false;
        });
        /*
      $("#yo_form").on("submit", function(event) {
          event.preventDefault();
          $("#yo_form").hide();
          $("#subscribers").hide();
          username = $("#username").val();
          url = $("#url").val();
          if(url==""){
           url = "http://seanssmith.me";
            }
            $.ajax({
                type: "POST",
                url: "/yo",
                data: {"username": username, "url": url},
                success: function(data){
                    $("#success").html("<h3 class=\"text-center\">"+data+"</h3>");
                }
            });
            return false;
        });
        */
    });
