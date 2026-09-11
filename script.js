const today = new Date();
const dateOptions = { year: 'numeric', month: 'short', day: 'numeric' };
const formattedDate = today.toLocaleDateString(undefined, dateOptions);
const dateValue = document.getElementById('todayDate');
if (dateValue) {
    dateValue.textContent = formattedDate;
}

const navLinks = Array.from(document.querySelectorAll('.nav-link'));
navLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        navLinks.forEach((item) => item.classList.toggle('active', item === link));
    });
});

const frameButtons = Array.from(document.querySelectorAll('.time-frame'));
frameButtons.forEach((button) => {
    button.addEventListener('click', () => {
        frameButtons.forEach((item) => item.classList.toggle('active', item === button));
    });
});

const chartSvg = document.querySelector('.chart-svg');
if (chartSvg) {
    chartSvg.animate([
        { transform: 'scaleY(0.98)', opacity: '0.8' },
        { transform: 'scaleY(1)', opacity: '1' }
    ], {
        duration: 700,
        iterations: 1,
        easing: 'ease-out'
    });
}
