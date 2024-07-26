document.getElementById('pingForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const target = document.getElementById('pingTarget').value;
    const response = await fetch(`/ping?target=${encodeURIComponent(target)}`);
    const data = await response.text();
    document.getElementById('pingResults').textContent = data;
});

document.getElementById('nmapForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const target = document.getElementById('nmapTarget').value;
    const response = await fetch(`/nmap?target=${encodeURIComponent(target)}`);
    const data = await response.text();
    document.getElementById('nmapResults').textContent = data;
});
