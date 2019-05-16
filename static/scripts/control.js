document.getElementById("send").onclick = function() {
    socket.emit("broadcast");
};
