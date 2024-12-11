// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
     anchor.addEventListener('click', function (e) {
         e.preventDefault();
         document.querySelector(this.getAttribute('href')).scrollIntoView({
             behavior: 'smooth'
         });
     });
 });
 
 // Toggle navigation for mobile view
 const navToggle = document.querySelector('.nav-toggle');
 const navLinks = document.getElementById('nav-links');
 
 navToggle.addEventListener('click', () => {
     navLinks.classList.toggle('nav-open');
 });
 
 // Close nav when a link is clicked
 navLinks.querySelectorAll('a').forEach(link => {
     link.addEventListener('click', () => {
         navLinks.classList.remove('nav-open');
     });
 });
 