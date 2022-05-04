let closeButton = document.querySelectorAll(".close-btn");
let items = document.querySelectorAll(".section ul li");

closeButton.forEach(element => {
    element.addEventListener("click", (event) => {
        let closedElement = items.filter(elem => event.target == elem);
        closedElement.classList.toggle(".show");
    })
});