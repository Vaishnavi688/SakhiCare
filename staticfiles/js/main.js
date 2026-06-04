// static/js/main.js
document.addEventListener("DOMContentLoaded", function(){
  document.querySelectorAll(".card-title").forEach(function(el){
    el.addEventListener("click", function(){
      const ul = el.nextElementSibling;
      if(!ul) return;
      if(ul.style.display === "none"){
        ul.style.display = "";
      } else {
        ul.style.display = "none";
      }
    });
  });
});
