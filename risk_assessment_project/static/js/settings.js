document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("settingorm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent default form submission

        let formData = {
            username: document.getElementById("username").value,
            email: document.getElementById("email").value,
        };

        fetch("/api/update-settings/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), // CSRF token for security
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Settings updated successfully!");
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    });
});

// Function to get CSRF token from cookies
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        document.cookie.split(";").forEach(cookie => {
            let trimmed = cookie.trim();
            if (trimmed.startsWith("csrftoken=")) {
                cookieValue = trimmed.substring("csrftoken=".length);
            }
        });
    }
    return cookieValue;
}
