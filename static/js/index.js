$("#search-icon").click(function() {
	$(".nav").toggleClass("search");
	$(".nav").toggleClass("no-search");
	$(".search-input").toggleClass("search-active");
  });
  
  $('.menu-toggle').click(function(){
	 $(".nav").toggleClass("mobile-nav");
	 $(this).toggleClass("is-active");
  });


function clicked(){
	console.log("clicked")
	location.href("dia_res.html")
}