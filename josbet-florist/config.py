#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuración de la aplicación Flask para Florería Josbet
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    """Configuración base"""
    FLASK_APP = 'run.py'
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta_josbet_2024')
    
    # Configuración de MySQL
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'floreria_josbet')
    DB_CHARSET = 'utf8mb4'
    
    # Rutas de archivos
    UPLOADS_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'static', 'uploads')
    IMAGES_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'static', 'images')
    
    # Configuración de Flask
    DEBUG = os.getenv('DEBUG', False)
    TESTING = False

class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configuración para pruebas"""
    DEBUG = True
    TESTING = True

# Seleccionar configuración según el ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
