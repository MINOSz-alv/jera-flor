# 🌸 Florería Josbet

Aplicación web Flask para gestión de una florería con carrito de compras, pedidos personalizados y panel de usuario.

## 📋 Características

- ✅ Autenticación de usuarios (registro/login)
- ✅ Catálogo de productos con imágenes
- ✅ Carrito de compras
- ✅ Pedidos personalizados
- ✅ Historial de pedidos
- ✅ Panel de usuario
- ✅ Gestión de base de datos MySQL

## 🏗️ Estructura del Proyecto

```
josbet-florist/
├── app/                           # Paquete principal de la aplicación
│   ├── __init__.py               # Factory de la aplicación Flask
│   ├── auth.py                   # Decoradores de autenticación
│   ├── database.py               # Funciones de conexión a BD
│   ├── utils.py                  # Utilidades y context processors
│   ├── routes/                   # Blueprints de rutas
│   │   ├── __init__.py
│   │   ├── auth.py              # Rutas: login, register, logout
│   │   ├── main.py              # Rutas: inicio, menú, carrito
│   │   └── orders.py            # Rutas: órdenes, checkout, pedidos personalizados
│   ├── templates/                # Plantillas HTML Jinja2
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── menu.html
│   │   ├── carrito.html
│   │   ├── checkout.html
│   │   ├── pedido-personalizado.html
│   │   ├── mis-pedidos.html
│   │   └── 404.html
│   ├── static/                   # Archivos estáticos
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   └── images/                   # Imágenes de productos
│
├── scripts/                       # Scripts de utilidad
│   ├── setup_db.py              # Crear BD y tablas
│   ├── update_images.py         # Actualizar imágenes
│   └── setup-create-folders.ps1 # Crear estructura Windows
│
├── config.py                      # Configuración de la aplicación
├── run.py                         # Punto de entrada
├── requirements.txt               # Dependencias Python
├── .env.example                   # Variables de entorno ejemplo
├── .gitignore                     # Git ignore
└── README.md                      # Este archivo
```

## 🚀 Instalación

### Requisitos
- Python 3.8+
- MySQL/XAMPP en ejecución
- pip (gestor de paquetes Python)

### Pasos

1. **Clonar o descargar el proyecto**
   ```bash
   cd josbet-florist
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Copiar .env.example a .env
   cp .env.example .env
   # Editar .env con tus datos de BD
   ```

5. **Crear base de datos**
   ```bash
   python scripts/setup_db.py
   ```

6. **Ejecutar la aplicación**
   ```bash
   python run.py
   ```

   La aplicación estará disponible en: **http://127.0.0.1:5000**

## 📁 Carpetas de Configuración

El script `scripts/setup-create-folders.ps1` (PowerShell) crea la estructura de carpetas necesarias:

```bash
.\scripts\setup-create-folders.ps1
```

## 🗄️ Base de Datos

Las tablas principales son:
- `usuarios` - Datos de clientes
- `productos` - Catálogo
- `carrito` - Items en carrito
- `pedidos` - Órdenes realizadas

Para resetear la BD:
```bash
python scripts/setup_db.py
```

## 🔑 Variables de Entorno (.env)

```env
FLASK_ENV=development
DEBUG=True
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=floreria_josbet
SECRET_KEY=clave_secreta_josbet_2024
```

## 📝 Uso

### Como usuario
1. Registrarse en `/register`
2. Iniciar sesión en `/login`
3. Explorar catálogo en `/menu`
4. Agregar productos al carrito
5. Completar compra en checkout
6. Ver historial en `/mis-pedidos`
7. Crear pedidos personalizados

### Como desarrollador
- Agregar nuevas rutas: crear archivo en `app/routes/`
- Registrar blueprint en `app/__init__.py`
- Modificar plantillas en `app/templates/`
- Agregar estilos en `app/static/css/`

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error de conexión a BD
- Verificar que MySQL está ejecutándose
- Revisar credenciales en `.env`
- Ejecutar `python scripts/setup_db.py`

### Puerto 5000 en uso
Cambiar en `run.py`:
```python
app.run(port=5001)
```

## 🔐 Seguridad

⚠️ **Importante para producción:**
- Cambiar `SECRET_KEY` en `.env`
- Usar variables de entorno seguras
- Encriptar contraseñas (usar bcrypt)
- Validar y sanitizar entradas
- Usar HTTPS

## 📄 Licencia

Proyecto educativo - Florería Josbet 2024-2026

## 👤 Autor

Desarrollado para Florería Josbet
