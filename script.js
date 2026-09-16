document.addEventListener('DOMContentLoaded', () => {
    // Configura a data alvo: 25 de Setembro de 2026, 23:59:59 (usando o ano atual para funcionar)
    // O sistema diz que a data atual é 15 de setembro de 2026
    const targetDate = new Date('2026-09-25T23:59:59').getTime();

    function updateCountdown() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
            // Se o tempo acabar
            const zeros = { days: '00', hours: '00', mins: '00', secs: '00' };
            setCountdownValues(zeros);
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        setCountdownValues({
            days: days.toString().padStart(2, '0'),
            hours: hours.toString().padStart(2, '0'),
            mins: minutes.toString().padStart(2, '0'),
            secs: seconds.toString().padStart(2, '0')
        });
    }

    function setCountdownValues(time) {
        // Top Banner
        document.getElementById('top-days').innerText = time.days;
        document.getElementById('top-hours').innerText = time.hours;
        document.getElementById('top-mins').innerText = time.mins;
        document.getElementById('top-secs').innerText = time.secs;

        // Main Hero
        document.getElementById('main-days').innerText = time.days;
        document.getElementById('main-hours').innerText = time.hours;
        document.getElementById('main-mins').innerText = time.mins;
        document.getElementById('main-secs').innerText = time.secs;
    }

    // Atualiza a cada 1 segundo
    setInterval(updateCountdown, 1000);
    updateCountdown(); // Chamada inicial
});
