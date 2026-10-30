# Registro de Productos

Aplicación de escritorio en **Python** con interfaz gráfica (**tkinter**) que permite registrar productos en una base de datos **MySQL**.

## Características

- Formulario simple para ingresar nombre, descripción, precio y stock.
- La **fecha de registro** se guarda automáticamente con la fecha del día.
- Validación de datos:
  - El nombre es obligatorio.
  - El precio debe ser un número y el stock un entero.
- Mensajes de aviso, error y confirmación con `messagebox`.
- Los campos se limpian después de guardar para registrar otro producto.

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

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <url-del-repositorio>
   cd <carpeta-del-proyecto>
   ```

2. Instala la dependencia:

   ```bash
   pip install pymysql
   ```

> `tkinter` ya viene incluido con Python en Windows. En Linux puede requerir `sudo apt install python3-tk`.

## Configuración de la base de datos

La tabla `productos` debe existir en la base `PFU_111_tienda`. Ejemplo de estructura:

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

Edita los datos de conexión al inicio del archivo `.py`:

```python
DB = dict(host="TU_HOST", user="TU_USUARIO", password="TU_CONTRASEÑA", database="tienda_db")
TABLA = "productos"
```

## Uso

Ejecuta el programa desde la terminal (Git Bash, CMD o PowerShell):

```bash
python nombre_del_archivo.py
```

1. Escribe el **nombre**, la **descripción**, el **precio** y el **stock**.
2. Presiona **Guardar producto**.
3. Verás el mensaje *"Producto guardado en la base de datos"* y el formulario quedará listo para un nuevo registro.

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

## Integrantes
Denilson Davis Machaca Flores 
Ronald Rruz Chino
Daniel Wilfredo Pomarez Huaranca
Jhilmar Jadiel Luna Gisbert

Proyecto desarrollado para la asignatura **PFU-111**.
