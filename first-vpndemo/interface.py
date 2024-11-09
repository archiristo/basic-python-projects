import tkinter as tk
from tkinter import messagebox
import sys
import os
import datavarutyun

def connect_to_vpn():
    server_address = entry_server.get()
    username = entry_username.get()
    password = entry_password.get()

    if server_address and username and password:
        # bağlantıyı simüle et
        messagebox.showinfo("Bağlandı", "Sunucuya bağlandı")
        os.system(r'python C:\Users\iris\OneDrive\Desktop\pyprojects\vpndemo\datavarutyun.py')
    else:
        messagebox.showerror("Hata", "Bağlantı hatası")

# anayüz hazırlığı

root = tk.Tk()
root.title("դատավարւտյւն")

# sunucu adresi
label_server = tk.Label(root, text="Sunucu adresi")
label_server.pack()
entry_server = tk.Entry(root)
entry_server.pack()

# kullanıcı adı
label_username = tk.Label(root, text="Kullanıcı adı")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# şifre
label_password = tk.Label(root, text="Şifre")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# buton
connect_button = tk.Button(root, text="Bağlan", command=connect_to_vpn)
connect_button.pack()

# kapanmasın.
root.mainloop()
