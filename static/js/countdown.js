document.addEventListener("DOMContentLoaded", function() {
    function updateCountdown() {
        fetch("/get_time_left")
            .then(response => response.json())
            .then(data => {
                let timeLeft = data.time_left;
                
                if (timeLeft <= 0) {
                    window.location.reload();
                    return;
                }
            
                let days = Math.floor(timeLeft / (60 * 60 * 24));
                let hours = Math.floor((timeLeft % (60 * 60 * 24)) / (60 * 60));
                let minutes = Math.floor((timeLeft % (60 * 60)) /60);
                let seconds = Math.floor(timeLeft % 60);
            
                document.getElementById("countdown").innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
                timeLeft--;
                setTimeout(updateCountdown, 1000);
        
            });
    }
    updateCountdown();
});