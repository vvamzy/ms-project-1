$(document).ready(function() {
    // Attach a click event handler to the fetch users button
    $("#fetch-users-btn").click(function() {
      // Make an AJAX request to the web service to fetch the users
      $.ajax({
        url: "http://localhost:5002/users",
        method: "GET",
        success: function(data) {
          // If the request was successful, display the users in the users div
          var users = JSON.parse(data);
          var usersHtml = "";
          for (var i = 0; i < users.length; i++) {
            var user = users[i];
            usersHtml += "<p>Name: " + user.name + ", Email: " + user.email + "</p>";
          }
          $("#users").html(usersHtml);
        },
        error: function(xhr, status, error) {
          // If the request failed, display an error message
          $("#users").html("<p>Error fetching users: " + error + "</p>");
        }
      });
    });
  });
  