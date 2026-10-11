import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry(f'600x500')
root.resizable(False,False)
root.iconbitmap("assets/image/icon.ico")
passkey = tk.StringVar()

canvas = tk.Canvas(root, width=600, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

bg_image = ImageTk.PhotoImage(Image.open("assets/image/bg.png"))
logo_image = ImageTk.PhotoImage(
    Image.open("assets/image/icon.png").convert("RGBA").resize((70, 70), Image.LANCZOS)
)

canvas.create_image(0, 0, image=bg_image, anchor="nw")
canvas.create_image(300, 100, image=logo_image, anchor="n")
canvas.create_text(300, 30, text="Personal Expense Tracker",
                   fill="white", font=("Segoe UI", 20, "bold"), anchor="n")

canvas.bg_image = bg_image      # keep references
canvas.logo_image = logo_image

passkey = ttk.Entry(canvas, textvariable=passkey, show="*")
passkey.place(x= 235, y= 190 )


root.mainloop()