 document.getElementById('maintenance-form').addEventListener('submit', function (event) {
      event.preventDefault();

      const formData = new FormData(this);

      fetch('/predict_maintenance_duration', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => response.json())
        .then(data => {
          document.getElementById('result').innerHTML = `Predicted Maintenance Duration: ${data.predicted_maintenance_duration}`;
        });
    });