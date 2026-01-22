#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Punto de entrada para la aplicación Flask
Ejecutar con: python run.py
"""

import os
from app import create_app

# Crear aplicación con configuración
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    print("✅ Iniciando Florería Josbet")
    print("📌 URL: http://127.0.0.1:5000")
    print("📌 Presiona Ctrl+C para detener")
    print()
    
    app.run(
        debug=app.config['DEBUG'],
        host='127.0.0.1',
        port=5000,
        use_reloader=True
    )
