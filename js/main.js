(function () {
  // Mobile menu toggle for all pages
  const navToggle = document.querySelector('[data-nav-toggle]');
  const navLinks = document.querySelector('[data-nav-links]');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
  }

  // Lightweight client-side feedback acknowledgement
  const feedbackForm = document.querySelector('[data-feedback-form]');
  if (feedbackForm) {
    feedbackForm.addEventListener('submit', function (event) {
      event.preventDefault();
      alert('Thanks for your feedback! We will review your message soon.');
      feedbackForm.reset();
    });
  }
})();
