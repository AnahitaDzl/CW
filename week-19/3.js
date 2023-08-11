
function setCookie(name, value, min) {
        var expiryDate = new Date();
        expiryDate.setTime(expiryDate.getTime() + (min * 60 * 1000));
        var expires = "expires=" + expiryDate.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
      }
function getCookie(name) {
        var cookieName = name + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var cookieArr = decodedCookie.split(';');
        for (var i = 0; i < cookieArr.length; i++) {
          var cookie = cookieArr[i];
          while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
          }
          if (cookie.indexOf(cookieName) == 0) {
            return cookie.substring(cookieName.length, cookie.length);
          }
        }
        return "";
      }
      

      var savedUsername = getCookie("username");
      if (savedUsername != "") {
        alert("Welcome back, " + savedUsername + "!");
      } else {

        var username = prompt("Please enter your name:");
        if (username != "" && username != null) {
          setCookie("username", username, 1);
          alert("Hello, " + username + "!");
        }
      }