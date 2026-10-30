
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

DB = dict(host="localhost", user="root", password="", database="tienda_db")
TABLA = "Productos"


def cargar():
    """Lee los registros de la base y los muestra en la tabla."""
    try:
        conn = pymysql.connect(**DB)
        with conn.cursor() as cur:
            cur.execute(
                f"SELECT id_producto, nombre, descripcion, precio, stock, fecha_registro "
                f"FROM {TABLA} ORDER BY id_producto"
            )
            filas = cur.fetchall()
        conn.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("Error de base de datos", str(e))
        return

    tabla.delete(*tabla.get_children())  # borra lo que había
    for fila in filas:
        tabla.insert("", "end", values=fila)

    lbl_total.config(text=f"Total de registros: {len(filas)}")


ventana = tk.Tk()
ventana.title("Productos registrados")
ventana.geometry("820x420")

columnas = ("id", "nombre", "descripcion", "precio", "stock", "fecha")
titulos = ("ID", "Nombre", "Descripción", "Precio", "Stock", "Fecha registro")
anchos = (50, 180, 280, 80, 70, 110)

contenedor = ttk.Frame(ventana, padding=10)
contenedor.pack(fill="both", expand=True)

tabla = ttk.Treeview(contenedor, columns=columnas, show="headings")
for col, titulo, ancho in zip(columnas, titulos, anchos):
    tabla.heading(col, text=titulo)
    tabla.column(col, width=ancho)

scroll = ttk.Scrollbar(contenedor, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll.set)

tabla.grid(row=0, column=0, sticky="nsew")
scroll.grid(row=0, column=1, sticky="ns")
contenedor.rowconfigure(0, weight=1)
contenedor.columnconfigure(0, weight=1)

pie = ttk.Frame(contenedor)
pie.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))
lbl_total = ttk.Label(pie, text="Total de registros: 0")
lbl_total.pack(side="left")
ttk.Button(pie, text="Actualizar", command=cargar).pack(side="right")

cargar()  # carga los datos al abrir
ventana.mainloop()