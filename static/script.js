function checkStatus() {
    fetch('/status')
    .then(response => response.json())
    .then(data => {
        let status = document.getElementById("statusIndicator");

        if (data.fall) {
            status.className = "fall";
            status.innerHTML = "🔴 FALL DETECTED!";
        } else {
            status.className = "safe";
            status.innerHTML = "🟢 SAFE";
        }
    });
}

setInterval(checkStatus, 1000);