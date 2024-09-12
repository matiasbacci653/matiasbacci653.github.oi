import tkinter as tk
from tkinter import messagebox
import requests

API_URL = 'http://127.0.0.1:5000/add-product'  # Cambia a la URL de tu backend

def add_product():
    name = name_entry.get()
    quantity = quantity_entry.get()
    if name and quantity:
        try:
            response = requests.post(API_URL, json={'name': name, 'quantity': int(quantity)})
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Producto añadido exitosamente")
                name_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Error al añadir producto: {response.status_code}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error en la solicitud: {e}")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Inventario")

tk.Label(root, text="Nombre del Producto:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Cantidad:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Añadir Producto", command=add_product).pack()

root.mainloop()