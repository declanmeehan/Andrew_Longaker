$(window).on('load resize', function(){
	$window = $(window);
	$('iframe').height(function(){
		return $window.height()-$(this).offset().top;
	});
}); 