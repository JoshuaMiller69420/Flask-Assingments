document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('toggleBtn');
    const navbar = document.getElementById('navbar');

    toggleBtn.addEventListener('click', () => {
        navbar.classList.toggle('hidden');
    });
});
