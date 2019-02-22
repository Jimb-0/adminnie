    
jQuery(document).ready(function (){
    var navOffset = jQuery(".navbar").offset().top;
    
    jQuery(".navbar").wrap('<div class="nav-placeholder"></div>');
    jQuery(".nav-placeholder").height(jQuery(".navbar").outerHeight());
    
    jQuery(".navbar").wrapInner('<div class="nav-inner"></div>');
    
    jQuery(window).scroll(function() {
        var scrollPos = jQuery(window).scrollTop();
        
        if (scrollPos >= navOffset) {
            jQuery(".navbar").addClass("fixed");
        } else {
            jQuery(".navbar").removeClass("fixed");
        }
    })
})


function myFunction() {
    var x = document.getElementById("navBar");
    if (x.className === "navbar" || x.className ==="navbar" + " fixed") {
        x.className += " responsive";
    } else if (x.className === "navbar" + " fixed" + " responsive") {
        x.className = " navbar" + " fixed";
    }
    else {
        x.className = "navbar";
    }
}