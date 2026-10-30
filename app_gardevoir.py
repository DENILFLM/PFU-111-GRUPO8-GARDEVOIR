import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import pymysql

# --- Cambia estos datos por los de tu base ---
DB = dict(host="10.0.16.154", user="pfu-111", password="SuperPassword123+", database="PFU_111_Tienda")
TABLA = "Productos"


def guardar():
    nombre = ent_nombre.get().strip()
    descripcion = ent_desc.get().strip()

    if not nombre:
        messagebox.showwarning("Falta dato", "Escribe el nombre del producto.")
        return
    try:
        precio = float(ent_precio.get())
        stock = int(ent_stock.get())
    except ValueError:
        messagebox.showwarning("Dato inválido", "Precio debe ser número y stock un entero.")
        return

    try:
        conn = pymysql.connect(**DB)
        with conn.cursor() as cur:
            cur.execute(
                f"INSERT INTO {TABLA} (nombre, descripcion, precio, stock, fecha_registro) "
                f"VALUES (%s, %s, %s, %s, %s)",
                (nombre, descripcion, precio, stock, date.today()),
            )
        conn.commit()
        conn.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("Error de base de datos", str(e))
        return

    messagebox.showinfo("Listo", "Producto guardado en la base de datos.")
    for e in (ent_nombre, ent_desc, ent_precio, ent_stock):
        e.delete(0, tk.END)
    ent_nombre.focus()


ventana = tk.Tk()
ventana.title("Registrar producto")
ventana.geometry("380x290")
ventana.resizable(False, False)

frm = ttk.Frame(ventana, padding=15)
frm.pack(fill="both", expand=True)
frm.columnconfigure(1, weight=1)

campos = ["Nombre:", "Descripción:", "Precio:", "Stock:"]
entradas = []
for i, texto in enumerate(campos):
    ttk.Label(frm, text=texto).grid(row=i, column=0, sticky="w", pady=6)
    e = ttk.Entry(frm)
    e.grid(row=i, column=1, sticky="ew", padx=(10, 0))
    entradas.append(e)
ent_nombre, ent_desc, ent_precio, ent_stock = entradas

ttk.Label(frm, text="La fecha de registro se guarda automáticamente.",
          foreground="gray").grid(row=4, column=0, columnspan=2, pady=(8, 0))

ttk.Button(frm, text="Guardar producto", command=guardar).grid(
    row=5, column=0, columnspan=2, pady=20)

ent_nombre.focus()
ventana.mainloop()
