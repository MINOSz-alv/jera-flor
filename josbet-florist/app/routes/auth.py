#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blueprint para rutas de autenticación
"""

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.database import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth')
def auth():
    """Página de selección de autenticación"""
    return render_template('auth.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login de usuario"""
    if request.method == 'POST':
        correo = request.form.get('correo', '')
        contrasena = request.form.get('contrasena', '')
        
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
            usuario = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if usuario and usuario['contrasena'] == contrasena:
                session['usuario_id'] = usuario['id']
                session['nombre'] = usuario['nombre']
                flash(f'¡Bienvenido {usuario["nombre"]}!', 'success')
                return redirect(url_for('main.menu'))
            else:
                flash('Correo o contraseña incorrectos', 'danger')
        except Exception as e:
            flash(f'Error de conexión: {str(e)}', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registro de usuario"""
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        correo = request.form.get('correo', '')
        contrasena = request.form.get('contrasena', '')
        
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
            
            if cursor.fetchone():
                flash('El correo ya está registrado', 'danger')
            else:
                cursor.execute(
                    'INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)',
                    (nombre, correo, contrasena)
                )
                conn.commit()
                flash('¡Registro exitoso! Ahora inicia sesión', 'success')
                cursor.close()
                conn.close()
                return redirect(url_for('auth.login'))
            
            cursor.close()
            conn.close()
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    """Cerrar sesión"""
    session.clear()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('main.index'))
