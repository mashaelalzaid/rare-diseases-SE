function message(status, id="") {
 
  document.getElementById("feedback").innerHTML = status;
 $("#feedback").show().delay(100000);
}

function error(type) {
  $("."+type).css("border-color", "#E14448");
}


$(document).ready(function() {
 
  $(document).on("click", "#signup-button", function() {
    $.post({
      type: "POST",
      url: "/",
      data: {"username": $("#signup-user").val()},
      success(response) {
        var status = JSON.parse(response)["status"];
        if (status === "query sent") { location.reload(); }
        else { message(status, "signup-box"); }
      }
    });
  });
});


