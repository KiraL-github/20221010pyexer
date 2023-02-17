const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

// 3sec 後行這個 function
setTimeout(function () {
  $("#message").fadeOut("slow");
}, 3000);

// $ -> j-Query
// # -> id
