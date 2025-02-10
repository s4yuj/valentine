function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "❤️"; // Heart character
    document.querySelector(".hearts-container").appendChild(heart);
    
    const size = Math.random() * 30 + 10;
    heart.style.fontSize = `${size}px`;
    heart.style.left = `${Math.random() * 100}vw`;
    heart.style.animationDuration = `${Math.random() * 3 + 2}s`;
    
    setTimeout(() => {
        heart.remove();
    }, 5000);
}

setInterval(createHeart, 50);
