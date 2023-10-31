import tkinter as tk
from tkinter import messagebox
import os, sys

def registrate():
    messagebox.showinfo('Registrate', 'Por favor, regístrate antes de continuar')

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == 'user' and password == 'pass':
        messagebox.showinfo('Login', 'Ingreso correcto')
    else:
        messagebox.showerror('Login', 'Usuario o contraseña incorrectos')

app = tk.Tk()
app.title('Login')
app.geometry('400x260')
app.configure(bg="#025E73")

label_username = tk.Label(app, text='Usuario')
label_username.pack(padx=0, pady=5)

entry_username = tk.Entry(app)
entry_username.pack(padx=20, pady=20)
# entry_username.place(x=25, y=10)

label_password = tk.Label(app, text='Contraseña')
label_password.pack()

entry_password = tk.Entry(app, show='*')
entry_password.pack(padx=20, pady=20)

button_login = tk.Button(app, text='Ingresar', command=login)
button_login.pack()

button_extra = tk.Button(app, text='Registrate', command=registrate)
button_extra.pack(padx=20, pady=20)

app.mainloop()