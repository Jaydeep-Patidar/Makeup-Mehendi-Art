// Add click functionality to service cards
document.addEventListener('DOMContentLoaded', () => {
    const serviceCards = document.querySelectorAll('.service-card');

    serviceCards.forEach(card => {
        card.addEventListener('click', () => {
            alert(`You selected the ${card.querySelector('h2').innerText} service!`);
        });
    });
});
