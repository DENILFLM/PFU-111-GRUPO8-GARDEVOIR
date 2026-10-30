# Registro de Productos

Aplicación de escritorio en **Python** con interfaz gráfica (**tkinter**) que permite registrar productos en una base de datos **MySQL**.

## Características

- Formulario para ingresar nombre, descripción, precio y stock.
- La **fecha de registro** se guarda automáticamente con la fecha del día.
- Validación: el nombre es obligatorio, el precio debe ser número y el stock un entero.
- Mensajes de aviso, error y confirmación con `messagebox`.
- Los campos se limpian después de guardar.

## Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3 | Lenguaje de programación |
| tkinter / ttk | Interfaz gráfica |
| PyMySQL | Conexión con MySQL |
| MySQL | Base de datos |

## Requisitos

- Python 3.8 o superior
- Acceso a un servidor MySQL con la base `tienda_db`
- Librería `pymysql`

## Guía paso a paso

### Paso 1. Verificar Python

```bash
python --version
```

Si da error, prueba con `py --version` o instala Python desde python.org (marca la casilla **Add Python to PATH**).

### Paso 2. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <carpeta-del-proyecto>
```

### Paso 3. Instalar la dependencia

```bash
pip install pymysql
```

> `tkinter` ya viene incluido con Python en Windows. En Linux: `sudo apt install python3-tk`.

### Paso 4. Crear la tabla en MySQL

Conéctate a tu servidor, selecciona la base `tienda_db` y ejecuta:

```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    fecha_registro DATE NOT NULL
);
```

### Paso 5. Configurar la conexión

Abre el archivo `.py` y edita los datos al inicio:

```python
DB = dict(host="TU_HOST", user="TU_USUARIO", password="TU_CONTRASEÑA", database="tienda_db")
TABLA = "productos"
```
### Paso 6. Ejecutar el programa

```bash
python nombre_del_archivo.py
```

Se abrirá la ventana **Registrar producto**.

### Paso 7. Registrar un producto

1. Escribe el **nombre** del producto.
2. Escribe la **descripción** (opcional).
3. Escribe el **precio** (ejemplo: `25.50`).
4. Escribe el **stock** (ejemplo: `10`).
5. Presiona **Guardar producto**.
6. Aparecerá el mensaje *"Producto guardado en la base de datos"* y el formulario quedará vacío.

### Paso 8. Verificar en la base de datos

```sql
SELECT * FROM productos;
```

## Subir el proyecto a GitHub

```bash
git init
git add .
git commit -m "Agrega app para registrar productos"
git remote add origin <url-del-repositorio>
git branch -M main
git push -u origin main
```

## Campos del formulario

| Campo | Tipo | Obligatorio |
|-------|------|-------------|
| Nombre | Texto | Sí |
| Descripción | Texto | No |
| Precio | Número decimal | Sí |
| Stock | Número entero | Sí |
| Fecha de registro | Automática | — |

## Posibles errores

| Mensaje | Causa probable |
|---------|----------------|
| *Falta dato* | El nombre está vacío |
| *Dato inválido* | El precio no es número o el stock no es entero |
| *Error de base de datos* | Servidor inaccesible, credenciales incorrectas o tabla inexistente |
| `ModuleNotFoundError: pymysql` | Falta ejecutar `pip install pymysql` |

## Integrantes
Denilson Davis Machaca Flores 
Ronald Rruz Chino
Daniel Wilfredo Pomarez Huaranca
Jhilmar Jadiel Luna Gisbert

Proyecto desarrollado para la asignatura **PFU-111**.
