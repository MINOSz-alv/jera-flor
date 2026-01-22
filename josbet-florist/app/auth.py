#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilidades de autenticación y decoradores
"""

from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    """Decorador para proteger rutas - requiere estar autenticado"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Debes iniciar sesión primero', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
