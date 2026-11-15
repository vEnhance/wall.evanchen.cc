document.querySelectorAll(".random-link").forEach((el) => {
  el.addEventListener("click", (e) => {
    e.preventDefault();
    const min = Number(el.dataset.min);
    const max = Number(el.dataset.max);
    const s = Math.floor(Math.random() * (max - min + 1)) + min;
    window.location.href = `/${s}/`;
  });
});
