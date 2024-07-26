document.getElementById('pingForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const target = document.getElementById('pingTarget').value;
    
    // Sending request without handling the response
    await fetch(`/ping?target=${encodeURIComponent(target)}`);
    
    // Optionally display a confirmation message
    alert(`Ping request sent to ${target}`);
});

document.getElementById('nmapForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const target = document.getElementById('nmapTarget').value;
    
    // Sending request without handling the response
    await fetch(`/nmap?target=${encodeURIComponent(target)}`);
    
    // Optionally display a confirmation message
    alert(`Nmap scan request sent to ${target}`);
});
