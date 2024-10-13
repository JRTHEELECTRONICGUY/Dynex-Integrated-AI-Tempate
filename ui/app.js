function sendRequest() {
    fetch("/api/request", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ api_key: "TEST_KEY_123", data: "Sample Data" })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = JSON.stringify(data);
    })
    .catch(error => console.error("Error:", error));
}
