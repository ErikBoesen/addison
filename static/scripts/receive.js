var sound = new Audio("/static/sound.wav");

onclick = function() {
    socket.on("play", function() {
        console.log("Playing sound.");
        sound.play().catch(function(e) { console.log(e) });
    });
};
