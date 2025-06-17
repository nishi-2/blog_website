document.querySelectorAll('.rule-button').forEach(button => {
    button.addEventListener('click', () => {
      console.log(`${button.textContent} clicked`);
    });
  });
  