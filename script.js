const urlInput = document.getElementById("urlInput");
const dataColor = document.getElementById("dataColor");
const finderColor = document.getElementById("finderColor");
const canvas = document.getElementById("qrCanvas");

function updateQR() {
  // Vérification que tout existe
  if (!urlInput || !canvas || !dataColor) return;

  const url = urlInput.value;
  if (!url) {
    const ctx = canvas.getContext("2d");
    if (ctx) ctx.clearRect(0, 0, canvas.width, canvas.height);
    return;
  }

  QRCode.toCanvas(canvas, url, {
    width: 220,
    margin: 1,
    color: {
      dark: dataColor.value,
      light: "#ffffff",
    },
  });
}

function downloadQR() {
  if (!canvas) return;
  const link = document.createElement("a");
  link.download = "qrcode.png";
  link.href = canvas.toDataURL();
  link.click();
}

urlInput?.addEventListener("input", updateQR);
dataColor?.addEventListener("input", updateQR);
finderColor?.addEventListener("input", updateQR);
