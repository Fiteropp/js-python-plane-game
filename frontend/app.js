const statusEl = document.getElementById("status");

async function checkHealth() {
  try {
    const res = await fetch("/api/health");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    statusEl.textContent = `OK (${data.status})`;
  } catch (err) {
    statusEl.textContent = `Offline (${err.message})`;
  }
}

checkHealth();
