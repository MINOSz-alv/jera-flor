#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blueprint para rutas principales
"""

from flask import Blueprint, render_template, send_from_directory, session, flash, redirect, url_for
import os
from app.database import get_db
from app.auth import login_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Página de inicio"""
    return render_template('index.html')

@main_bp.route('/images/<path:filename>')
def serve_image(filename):
    """Servir imágenes de la carpeta images/"""
    images_dir = os.path.join(os.path.dirname(__file__), '..', 'images')
    return send_from_directory(images_dir, filename)

@main_bp.route('/menu')
@login_required
def menu():
    """Menú de productos"""
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('menu.html', productos=productos)
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return render_template('menu.html', productos=[])

@main_bp.route('/carrito')
@login_required
def carrito():
    """Mostrar carrito de compras"""
    usuario_id = session['usuario_id']
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.id, p.id as producto_id, p.nombre, p.precio, c.cantidad
            FROM carrito c
            JOIN productos p ON c.producto_id = p.id
            WHERE c.usuario_id = %s
        """, (usuario_id,))
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        
        total = sum(item['precio'] * item['cantidad'] for item in items) if items else 0
        return render_template('carrito.html', items=items, total=total)
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return render_template('carrito.html', items=[], total=0)
