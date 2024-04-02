try {
  AOS.init({
    duration: 1000,
  });
} catch (error) {
  console.log(error);
}

/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
};

/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navLinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
};

addEventOnElem(navTogglers, "click", toggleNavbar);

const closeNavbar = function () {
  navbar.classList.remove("active");
  overlay.classList.remove("active");
};

addEventOnElem(navLinks, "click", closeNavbar);

/**
 * header active when scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElem = function () {
  if (window.scrollY > 80) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
};

addEventOnElem(window, "scroll", activeElem);

const video = document.getElementById("video");
const playButton = document.getElementById("playButton");

// Add click event listener to the play button
playButton.addEventListener("click", function () {
  if (video.paused) {
    video.play();
    playButton.innerHTML = '<i class="bx bx-pause"></i>';
  } else {
    video.pause();
    playButton.innerHTML = '<i class="bx bx-play"></i>';
  }
});

// Add event listener to detect when the video ends
video.addEventListener("ended", function () {
  // Reset the button icon to play
  playButton.innerHTML = '<i class="bx bx-play"></i>';
});

/* ================= Swiper Featured ==================*/
try {
  var slider = tns({
    container: ".services-slide",
    items: 3,
    rewind: true,
    swipeAngle: false,
    speed: 400,
    mouseDrag: true,
    responsive: {
      100: {
        items: 1,
      },
      200: {
        items: 1,
      },
      300: {
        items: 1,
      },

      400: {
        items: 1,
      },

      500: {
        items: 1,
      },

      600: {
        items: 1,
      },
      650: {
        items: 1,
      },
      700: {
        items: 1,
      },

      800: {
        items: 2,
      },
      900: {
        items: 2,
      },
      1200: {
        items: 3,
      },
    },
  });
} catch (error) {
  console.log(error);
}
