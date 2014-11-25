    $(document).ready(function() {
        /*
	$.get("/subscriber_count", function(data){
            console.log(data)
            $("#subscribers").html("<h3 class=\"text-center\">"+data+" Subscribers</h3>");
        });
	*/
    if(getUrlParameter("username") != ""){
        $("#username").val(getUrlParameter("username"));
    }
    if(getUrlParameter("name") != ""){
        $("#name").val(getUrlParameter("name"));
    }

    function getUrlParameter(sParam)
    {
        var sPageURL = window.location.search.substring(1);
        var sURLVariables = sPageURL.split('&');
        for (var i = 0; i < sURLVariables.length; i++)
            {
                var sParameterName = sURLVariables[i].split('=');
                if (sParameterName[0] == sParam)
                    {
                        return sParameterName[1];
                    }
            }
        return "";
    }



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
    });
