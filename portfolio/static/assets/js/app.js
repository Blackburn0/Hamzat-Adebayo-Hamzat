const menu = document.querySelector("#menu");
const navbar = document.querySelector("#navbar");
const close = document.querySelector("#close");

menu.addEventListener('click', function () {
    navbar.classList.remove("hidden");
});

close.addEventListener('click', function () {
    navbar.classList.add("hidden");
});


