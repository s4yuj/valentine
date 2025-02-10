document.addEventListener("DOMContentLoaded", function() {
    function updateCountdown() {
        const now = Math.floor(Date.now() / 1000);
        let timeLeft = valentinesDay - now;

        if (timeLeft <= 0) {
            window.location.reload();
            return;
        }
    
        let days = Math.floor(timeLeft / (60 * 60 * 24));
        let hours = Math.floor((timeLeft % (60 * 60 * 24)) / (60 * 60));
        let minutes = Math.floor((timeLeft % (60 * 60)) / 60);
        let seconds = Math.floor(timeLeft % 60);

        days = days < 10 ? '0' + days : days;
        hours = hours < 10 ? '0' + hours : hours;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;

        document.getElementById('days').innerHTML = days;
        document.getElementById('hours').innerHTML = hours;
        document.getElementById('minutes').innerHTML = minutes;
        document.getElementById('seconds').innerHTML = seconds;
    
        timeLeft--;
        setTimeout(updateCountdown, 1000);
    }
    updateCountdown();
});