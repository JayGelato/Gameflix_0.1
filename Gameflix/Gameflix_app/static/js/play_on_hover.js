let clips = document.querySelectorAll(".vid");

clips.forEach(function (clip) {
  clip.addEventListener("mouseover", function () {
    clip.play();
  });

  clip.addEventListener("mouseout", function () {
    clip.pause();
    clip.currentTime = 0;
  });
});
