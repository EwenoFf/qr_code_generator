import segno
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter import colorchooser
from PIL import Image, ImageTk

# Variables globales
qr_image = None
color_data = "#56cfe1"
color_finder = "#5390d9"

def update_qr(event=None):
    global qr_image

    url = url_entry.get()
    if not url:
        qr_label.config(image="")
        return

    qr = segno.make_qr(url)
    qr.save(
        "preview.png",
        scale=6,
        dark=color_finder,
        data_dark=color_data,
        light="white"
    )

    img = Image.open("preview.png").resize((220, 220))
    qr_image = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_image)

def choose_data_color():
    global color_data
    color = colorchooser.askcolor(title="Couleur des données")
    if color[1]:
        color_data = color[1]
        update_qr()

def choose_finder_color():
    global color_finder
    color = colorchooser.askcolor(title="Couleur des repères")
    if color[1]:
        color_finder = color[1]
        update_qr()

def save_qr():
    url = url_entry.get()
    if not url:
        Messagebox.show_error("Erreur", "Veuillez entrer une URL")
        return

    qr = segno.make_qr(url)
    qr.save(
        "qrcode.png",
        scale=12,
        dark=color_finder,
        data_dark=color_data,
        light="white"
    )

    Messagebox.show_info("Succès", "QR Code sauvegardé (qrcode.png)")

# Fenêtre principale
app = ttk.Window(themename="superhero")
app.title("QR Code Generator")
app.geometry("480x620")
app.resizable(False, False)

# Titre
ttk.Label(
    app,
    text="QR Code Generator",
    font=("Helvetica", 20, "bold")
).pack(pady=20)

# URL
url_frame = ttk.Frame(app)
url_frame.pack(padx=30, fill="x")

ttk.Label(url_frame, text="URL").pack(anchor="w")
url_entry = ttk.Entry(url_frame)
url_entry.pack(fill="x", pady=5)
url_entry.bind("<KeyRelease>", update_qr)

# Couleurs
color_frame = ttk.LabelFrame(app, text="Couleurs du QR Code")
color_frame.pack(padx=30, pady=15, fill="x")

ttk.Button(
    color_frame,
    text="Couleur des données",
    command=choose_data_color
).pack(fill="x", pady=5)

ttk.Button(
    color_frame,
    text="Couleur des repères",
    command=choose_finder_color
).pack(fill="x", pady=5)

# Carte QR
card = ttk.Frame(app, padding=15, bootstyle="dark")
card.pack(pady=20)

qr_label = ttk.Label(card)
qr_label.pack()

# Sauvegarde
ttk.Button(
    app,
    text="Sauvegarder le QR Code",
    command=save_qr,
    bootstyle="primary",
    width=30
).pack(pady=20)

app.mainloop()
