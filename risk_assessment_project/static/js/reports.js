document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById("riskChart").getContext("2d");
    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["High Risk", "Medium Risk", "Low Risk"],
            datasets: [{
                label: "Businesses",
                data: [5, 10, 15],
                backgroundColor: ["#dc3545", "#ffc107", "#28a745"],
            }]
        }
    });
});
