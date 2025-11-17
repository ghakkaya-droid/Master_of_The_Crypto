#TODO: "Entrylerden bilgi toparlama"
#TODO: "Encrypt ve Decrypt öğren"

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pathlib import Path
from simplecrypt import encrypt,decrypt

file_path = Path("mysecret.txt")

def get_title(path):
    if not path.exists():
        path.touch()
    if Entry_Title.get().strip() == "" or Text_Secret.get("1.0","end").strip() == "":
        messagebox.showwarning("Warning", "Please enter a valid title")

    with path.open("a", encoding="utf-8") as f:
        f.write(title.get()+"\n")
        f.write(Text_Secret.get("1.0", "end")+"\n")


# Ana Ekran Düzenleme
window = tk.Tk()
window.title("Secret Notes")
window.minsize(400, 780)
window.config(padx=15, pady=15,bg="light grey")

title = tk.StringVar()

# Ana Ekrana Label içerisinde Resim yerleştirme
file_path_photo = "Photo_TopSecret.jpg"

image = Image.open(file_path_photo)
image = image.resize((200, 200))

photo = ImageTk.PhotoImage(image)
Label_TopSecret = tk.Label(window, image=photo)
Label_TopSecret.place(x=90,y=5)
window.img_ref = photo

# Ana Ekranda gerekli nesneler

Label_EnterYourTitle = tk.Label(text ="Enter your Title",font=("Arial", 12,"bold"),bg="light grey")
Label_EnterYourTitle.place(x=136,y=210)

Entry_Title = tk.Entry(window,width=30,font=("Arial", 12,"normal"),bg="white",textvariable=title)
Entry_Title.place(x=50,y=235)

Label_EnterYorSecret =tk.Label(text="Enter your secret",font=("Arial", 12,"bold"),bg="light grey")
Label_EnterYorSecret.place(x=125,y=260)

Text_Secret = tk.Text(font=("Arial", 12,"normal"),bg="white",width=30,height=15)
Text_Secret.place(x=50,y=290)

Label_MasterKey =tk.Label(text="Enter your master key",font=("Arial", 12,"bold"),bg="light grey")
Label_MasterKey.place(x=105,y=570)

Entry_MasterKey = tk.Entry(width=30,font=("Arial", 12,"normal"),bg="white")
Entry_MasterKey.place(x=50,y=595)

save_button = tk.Button(text="Save&Enrypt",font=("Arial",9,"bold"),bg="white",width=20,command=lambda:get_title(file_path))
save_button.place(x=120,y=630)

decrypt_button = tk.Button(text="Dectypt",font=("Arial",9,"bold"),bg="white",width=20)
decrypt_button.place(x=120,y=670)


window.mainloop()
