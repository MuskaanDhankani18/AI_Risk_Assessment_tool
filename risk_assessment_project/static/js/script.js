// document.addEventListener("DOMContentLoaded", function () {
//     document.getElementById("business-form").addEventListener("submit", async function (event) {
//         event.preventDefault();  // Prevent page reload

//         const formData = {
//             business_name: document.getElementById("business_name")?.value?.trim() || null,
//             industry: document.getElementById("industry")?.value?.trim() || null,
//             revenue: document.getElementById("revenue")?.value ? parseFloat(document.getElementById("revenue").value) : null,
//             employees: document.getElementById("employees")?.value ? parseInt(document.getElementById("employees").value) : null,
//             location: document.getElementById("location")?.value?.trim() || null,
//             financial_stability: document.getElementById("financial_stability")?.value ? parseInt(document.getElementById("financial_stability").value) : null,
//             market_risk: document.getElementById("market_risk")?.value ? parseInt(document.getElementById("market_risk").value) : null,
//             operational_risk: document.getElementById("operational_risk")?.value ? parseInt(document.getElementById("operational_risk").value) : null,
//             cybersecurity_risk: document.getElementById("cybersecurity_risk")?.value ? parseInt(document.getElementById("cybersecurity_risk").value) : null,
//             compliance_risk: document.getElementById("compliance_risk")?.value ? parseInt(document.getElementById("compliance_risk").value) : null,
//             description: document.getElementById("description")?.value?.trim() || null
//         };

//         console.log("Submitting data:", formData);  // Debugging

//         // Ensure no required fields are missing
//         for (let key in formData) {
//             if (formData[key] === null || formData[key] === "") {
//                 alert(`Please fill in the ${key} field.`);
//                 return;
//             }
//         }

//         try {
//             let response = await fetch("/api/add-business/", {
//                 method: "POST",
//                 headers: {
//                     "Content-Type": "application/json",
//                     "X-CSRFToken": getCSRFToken()
//                 },
//                 body: JSON.stringify(formData)
//             });

//             let responseData = await response.json();
//             console.log("Server Response:", responseData);

//             if (!response.ok) throw new Error(responseData.error || "Bad Request");

//             alert("Business Added Successfully!");
//             window.location.href = "/dashboard/";
//         } catch (error) {
//             console.error("Error:", error);
//             alert("Error submitting form: " + error.message);
//         }
//     });
// });

// // Function to get CSRF token from cookies
// function getCSRFToken() {
//     return document.cookie.split("; ")
//         .find(row => row.startsWith("csrftoken="))
//         ?.split("=")[1] || "";
// }



document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("business-form").addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = {
            business_name: document.getElementById("business_name").value.trim(),
            industry: document.getElementById("industry").value.trim(),
            revenue: parseFloat(document.getElementById("revenue").value),
            employees: parseInt(document.getElementById("employees").value),
            location: document.getElementById("location").value.trim(),
            financial_stability: parseInt(document.getElementById("financial_stability").value),
            market_risk: parseInt(document.getElementById("market_risk").value),
            operational_risk: parseInt(document.getElementById("operational_risk").value),
            cybersecurity_risk: parseInt(document.getElementById("cybersecurity_risk").value),
            compliance_risk: parseInt(document.getElementById("compliance_risk").value),
            description: document.getElementById("description").value.trim(),
        };

        try {
            let response = await fetch("/api/add-business/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify(formData)
            });

            let responseData = await response.json();
            if (!response.ok) throw new Error(responseData.error || "Bad Request");

            alert("Business Added Successfully!");
            window.location.href = "/dashboard/";
        } catch (error) {
            console.error("Error:", error);
            alert("Error submitting form: " + error.message);
        }
    });
});

// Function to get CSRF token from cookies
function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1] || "";
}
