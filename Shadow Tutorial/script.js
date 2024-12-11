document.addEventListener('DOMContentLoaded', function() {
     // Smooth scrolling for anchor links within the same page
     const links = document.querySelectorAll('nav ul li a');
 
     for (const link of links) {
         link.addEventListener('click', function(event) {
             // Check if the link is an internal link
             const isInternalLink = this.getAttribute('href').startsWith('#');
 
             if (isInternalLink) {
                 smoothScroll(event);
             }
         });
     }
 
     function smoothScroll(event) {
         event.preventDefault();
 
         const targetId = event.currentTarget.getAttribute('href').substring(1);
         const targetElement = document.getElementById(targetId) || document.getElementsByTagName('header')[0];
         
         window.scrollTo({
             top: targetElement.offsetTop,
             behavior: 'smooth'
         });
     }
 });
 