#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilidades de base de datos para la aplicación
"""

import pymysql
from flask import current_app

def get_db_config():
    """Obtiene la configuración de BD desde la app"""
    return {
        'host': current_app.config['DB_HOST'],
        'user': current_app.config['DB_USER'],
        'password': current_app.config['DB_PASSWORD'],
        'database': current_app.config['DB_NAME'],
        'charset': current_app.config['DB_CHARSET'],
        'cursorclass': pymysql.cursors.DictCursor
    }

def get_db():
    """Crear conexión a la BD"""
    return pymysql.connect(**get_db_config())
