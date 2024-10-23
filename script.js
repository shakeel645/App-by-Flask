// static/script.js
document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const dataInput = document.getElementById('data').value;
    
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: dataInput })
    })
    .then(response => response.json())
    .then(data => {
        location.reload(); // Reload to display new data
    })
    .catch(error => console.error('Error:', error));
});
