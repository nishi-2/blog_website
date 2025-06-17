// main_page_js.js
document.addEventListener("DOMContentLoaded", () => {
  // Animate text elements
  const animatedTextElements = document.querySelectorAll(".animated-text");
  animatedTextElements.forEach((el, index) => {
    el.style.opacity = 0;
    el.style.transform = "translateY(20px)";
    setTimeout(() => {
      el.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
      el.style.opacity = 1;
      el.style.transform = "translateY(0)";
    }, 300 * index);
  });

  const title = document.getElementById("animated-title");
  if (title) {
    title.style.opacity = 0;
    title.style.transform = "scale(0.8)";
    setTimeout(() => {
      title.style.transition = "opacity 1s ease, transform 1s ease";
      title.style.opacity = 1;
      title.style.transform = "scale(1)";
    }, 500);
  }

  const chooseText = document.querySelector(".select-title");
  if (chooseText) {
    chooseText.style.opacity = 0;
    chooseText.style.transform = "translateY(20px)";
    setTimeout(() => {
      chooseText.style.transition = "opacity 1s ease, transform 1s ease";
      chooseText.style.opacity = 1;
      chooseText.style.transform = "translateY(0)";
    }, 1200);
  }

  // Handle form submission
  const form = document.querySelector('.queryForm');
  const popup = document.getElementById("popup");
  const popupMessage = document.getElementById("popup-message");
  const closeBtn = document.getElementById("close-popup");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(this);

      fetch("/submit", {
        method: "POST",
        body: formData,
      })
        .then((res) => res.json())
        .then((data) => {
          popupMessage.innerText = data.message;
          popup.style.display = "block";
        })
        .catch((err) => {
          popupMessage.innerText = "Submission failed. Try again.";
          popup.style.display = "block";
        });
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      popup.style.display = "none";
      if (form) form.reset();
    });
  }
});
