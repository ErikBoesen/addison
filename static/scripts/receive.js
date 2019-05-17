var sound = new Audio("/static/sound.wav");

document.getElementById("accept").onclick = function() {
    document.getElementById("information").style.display = "none";
    document.getElementById("preparation").style.display = "block";
    socket.on("play", function() {
        console.log("Playing sound.");
        sound.play().catch(function(e) { console.log(e) });
    });
};
