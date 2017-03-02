console.log("hello")

var requestUri = new Windows.Foundation.Uri("https://www.facebook.com/v2.8/dialog/oauth?client_id=1245225482240854=&display=popup&response_type=token");
    //&redirect_uri=ms-app://{package-security-identifier}

Windows.Security.Authentication.Web.WebAuthenticationBroker.authenticateAsync(
  options,
  requestUri)
  .done(function (result) {
    // Handle the response from the Login Dialog
  }
);
