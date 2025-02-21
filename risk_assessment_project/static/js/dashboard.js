document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/businesses/')
        .then(response => response.json())
        .then(data => {
            let businesses = data.businesses;
            let labels = [];
            let riskScores = [];
            let financialRisks = [];
            let marketRisks = [];
            let operationalRisks = [];

            businesses.forEach(business => {
                labels.push(business.business_name);
                riskScores.push(business.risk_score || 0);
                financialRisks.push(business.financial_stability || 0);
                marketRisks.push(business.market_risk || 0);
                operationalRisks.push(business.operational_risk || 0);
            });

            // Risk Score Distribution Chart
            new Chart(document.getElementById('riskChart'), {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Risk Score',
                        data: riskScores,
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: { y: { beginAtZero: true } }
                }
            });

            // Risk Factors Breakdown Chart
            new Chart(document.getElementById('riskFactorsChart'), {
                type: 'radar',
                data: {
                    labels: ['Financial Stability', 'Market Risk', 'Operational Risk'],
                    datasets: [{
                        label: 'Risk Factors',
                        data: [financialRisks.reduce((a, b) => a + b, 0) / businesses.length, 
                               marketRisks.reduce((a, b) => a + b, 0) / businesses.length, 
                               operationalRisks.reduce((a, b) => a + b, 0) / businesses.length],
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true
                }
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});
