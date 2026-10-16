import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from assets.Place_holder import PLH
import json
from pathlib import Path

root = tk.Tk()
root.title("Expense Tracker")
root.geometry(f'600x500')
root.resizable(False,False)
root.iconbitmap("assets/image/icon.ico")
#var
Passkey = tk.StringVar()
Date = tk.StringVar()
Amount = tk.StringVar()
# User Login.
style1 = ttk.Style()
style1.theme_use("clam")
style1.configure("Custom.TEntry", fieldbackground="#1e3a45", foreground="White")
frame1 = ttk.Frame(root)
frame1.pack(fill="both", expand=True)
canvas = tk.Canvas(frame1, width=600, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)

bg_image = ImageTk.PhotoImage(Image.open("assets/image/bg.png"))
logo_image = ImageTk.PhotoImage(Image.open("assets/image/icon.png").convert("RGBA").resize((70, 70), Image.LANCZOS))
logo_lock = ImageTk.PhotoImage(Image.open("assets/image/locklogo.png").convert("RGBA").resize((30, 30), Image.LANCZOS))

canvas.create_image(0, 0, image=bg_image, anchor="nw")
canvas.create_image(300, 100, image=logo_image, anchor="n")
canvas.create_image(210, 185, image=logo_lock, anchor="n")
canvas.create_text(300, 30, text="Personal Expense Tracker",
                   fill="white", font=("Segoe UI", 20, "bold"), anchor="n")

canvas.bg_image = bg_image      # keep references
canvas.logo_image = logo_image

passkey = ttk.Entry(canvas, textvariable=Passkey, show="★ ", style = "Custom.TEntry",justify='center')
passkey.place(x= 235, y= 190 )

# def for new pages
def Newpage( title):
    frame = ttk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=500, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.create_text(300, 30, text= f'{title}',
                    fill="white", font=("Segoe UI", 20, "bold"), anchor="n")
    return canvas, frame


#Dashboard

canvas2, frame2 = Newpage("Dashboard")

style2=ttk.Style()
style2.theme_use('clam')
style2.configure(
    'Custom.TButton', 
    background= "#050505",
    foreground='white', 
    font=('Helvetica', 12, 'bold'))

#add new expenses

def add():
    frame2.pack_forget()
    canvas3,frame3 = Newpage("Add new expenses")
    date = PLH(canvas3, "Date", Date, 300, 100)
    description = tk.Text(canvas3, width=40, height=5, foreground="White", background="#1e3a45",  borderwidth=2,
                                                                                            relief="solid",
                                                                                            highlightthickness=1,
                                                                                            highlightbackground="white",
                                                                                            highlightcolor="white")
    description.insert("1.0","How did you spend your money,\ndiscribeit on me!")
    description.place(x=300,y=150, anchor="n")
    frame3.pack(fill="both", expand=True)

    canvas3.create_text(300, 260, text="Choose your category here:",anchor='n', fill="white")

    Categories = ttk.Combobox(canvas3, values=("Food","Transport", "Education", "Shopping", "Bills", "Others"))
    Categories.place(x=300, y = 290, anchor='n')

    amount = PLH(canvas3, "Amount", Amount, 300, 330)

    #saving data in json

    category = Categories.get()
    Description = description.get()

    new_expense = {"Date" : Date, "Description" : Description, "Category" : category, "Amount" : Amount}

    


    save = ttk.Button(canvas3, text="Save", style="Custom.TButton")
    save.place(x=300, y= 400, anchor='n')

    
    
    
add = ttk.Button(canvas2, text="✅ Add new expenses", style="Custom.TButton", command=add )
add.place(x = 300, y = 100, anchor='n')
view = ttk.Button(canvas2, text="✅ View all expenses", style="Custom.TButton" )
view.place(x = 300, y = 175, anchor='n')
update = ttk.Button(canvas2, text="✅ Update existing expenses", style="Custom.TButton" )
update.place(x = 300, y = 250, anchor='n')

style3=ttk.Style()
style3.theme_use('clam')
style3.configure(
    'logout.TButton', 
    background= "#160F65",
    foreground="#EEDFDE", 
    font=('arial', 8, 'bold')
)


def CheckPasskey(Password):
    
    if(Password.get() == "17794"):
        print("OK")
        Passkey.set("")
        frame1.pack_forget()
        frame2.pack(fill='both', expand=True)
        
    else:
        print("NO")
        Passkey.set("")

def logout():
    
    result=messagebox.askokcancel("Are you sure?", "Sure?", parent=frame2)
    if result:
        frame2.pack_forget()
        frame1.pack()
    else:
        pass
    

log_out = ttk.Button(canvas2, text="Logout", style="logout.TButton", command=logout)
log_out.place(x=0, y=0)
enter = ttk.Button(canvas, text="ENTER", command=lambda: CheckPasskey(Passkey))
enter.place(x=258,y= 250)


root.mainloop()