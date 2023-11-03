from tkinter import *

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # Leer el archivo .txt
    with open('user_data.txt', 'r') as file:
        lines = file.readlines()

    # Verificar si el usuario ingresado existe en el archivo
    for line in lines:
        data = line.split()
        if data[0] == username and data[1] == password:
            result.set("Usuario encontrado")
            return

    result.set("Usuario no encontrado")

# Crear la ventana principal
root = Tk()
root.title("Login")

# Crear los campos de entrada para el nombre de usuario y la contraseña
username_entry = Entry(root)
username_entry.pack()

password_entry = Entry(root)
password_entry.pack()

# Crear el botón de inicio de sesión
login_button = Button(root, text="Login", command=check_login)
login_button.pack()

# Crear un mensaje que se mostrará al usuario
result = StringVar()
result_label = Label(root, textvariable=result)
result_label.pack()

root.mainloop()