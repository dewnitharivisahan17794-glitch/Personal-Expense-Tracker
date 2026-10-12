import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry(f'600x500')
root.resizable(False,False)
root.iconbitmap("assets/image/icon.ico")
Passkey = tk.StringVar()
# User Login.
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.TEntry", fieldbackground="#1e3a45", foreground="White")
frame1 = ttk.Frame(root)
frame1.pack(fill="both", expand=True)
canvas = tk.Canvas(frame1, width=600, height=500, highlightthickness=0)
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

passkey = ttk.Entry(canvas, textvariable=Passkey, show="★ ", style = "Custom.TEntry",justify='center')
passkey.place(x= 235, y= 190 )

# def for new pages
def Newpage(parent, title):
    canvas = tk.Canvas(parent, width=600, height=500, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.create_text(300, 30, text= f'{title}',
                    fill="white", font=("Segoe UI", 20, "bold"), anchor="n")
    return canvas


#Dashboard
frame2 = ttk.Frame()
Newpage(frame2, "Dashboard")
def CheckPasskey(Password):
    
    if(Password.get() == "17794"):
        print("OK")
        Passkey.set("")
        frame1.forget()
        frame2.pack(fill='both', expand=True)
        
    else:
        print("NO")
        Passkey.set("")

enter = ttk.Button(canvas, text="ENTER", command=lambda: CheckPasskey(Passkey))
enter.place(x=258,y= 250)




root.mainloop()