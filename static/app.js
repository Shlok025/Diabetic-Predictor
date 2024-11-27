document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('risk-form');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const data = {
                Pregnancy: document.getElementById('Pregnancy').value,
                Plasma: document.getElementById('Plasma').value,
                BloodPressure: document.getElementById('BloodPressure').value,
                Skin: document.getElementById('Skin').value,
                Test: document.getElementById('Test').value,
                BMI: document.getElementById('BMI').value,
                DBF: document.getElementById('DBF').value,
                Age: document.getElementById('Age').value
            };

            fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = `Prediction: ${data.risk_score}`;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    } else {
        console.error('Form with ID "risk-form" not found.');
    }
});