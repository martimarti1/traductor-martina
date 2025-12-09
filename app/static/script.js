async function traducir() {
    const texto = document.getElementById("entrada").value;
    const modo = document.getElementById("modo").value;

    const response = await fetch("/api/traducir", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto: texto, modo: modo })
    });

    const data = await response.json();
    document.getElementById("salida").innerText = data.traduccion;
}
