#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blueprint para rutas de órdenes y carrito
"""

from flask import Blueprint, request, session, flash, redirect, url_for, render_template
from app.database import get_db
from app.auth import login_required

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/agregar-carrito/<int:producto_id>', methods=['POST'])
@login_required
def agregar_carrito(producto_id):
    """Agregar producto al carrito"""
    usuario_id = session['usuario_id']
    cantidad = request.form.get('cantidad', 1, type=int)
    
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT * FROM carrito WHERE usuario_id = %s AND producto_id = %s',
            (usuario_id, producto_id)
        )
        item = cursor.fetchone()
        
        if item:
            cursor.execute(
                'UPDATE carrito SET cantidad = cantidad + %s WHERE usuario_id = %s AND producto_id = %s',
                (cantidad, usuario_id, producto_id)
            )
        else:
            cursor.execute(
                'INSERT INTO carrito (usuario_id, producto_id, cantidad) VALUES (%s, %s, %s)',
                (usuario_id, producto_id, cantidad)
            )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Producto agregado al carrito', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    
    return redirect(url_for('main.menu'))

@orders_bp.route('/eliminar-carrito/<int:item_id>', methods=['POST'])
@login_required
def eliminar_carrito(item_id):
    """Eliminar producto del carrito"""
    usuario_id = session['usuario_id']
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM carrito WHERE id = %s AND usuario_id = %s', (item_id, usuario_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Producto eliminado del carrito', 'info')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    
    return redirect(url_for('main.carrito'))

@orders_bp.route('/pedido-personalizado', methods=['GET', 'POST'])
@login_required
def pedido_personalizado():
    """Crear pedido personalizado"""
    if request.method == 'POST':
        usuario_id = session['usuario_id']
        tipo_flor = request.form.get('tipo', '')
        color = request.form.get('color', '')
        cantidad = request.form.get('cantidad', 1)
        mensaje = request.form.get('mensaje', '')
        extra_kit = request.form.get('extraKit', 'ninguno')
        extra = request.form.get('extra', '')
        
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pedidos (usuario_id, tipo_flor, color, cantidad, mensaje, extra_kit, extra, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, 'pendiente')
            """, (usuario_id, tipo_flor, color, cantidad, mensaje, extra_kit, extra))
            
            conn.commit()
            pedido_id = cursor.lastrowid
            cursor.close()
            conn.close()
            
            flash(f'¡Pedido #{pedido_id} creado exitosamente!', 'success')
            return redirect(url_for('orders.mis_pedidos'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('pedido-personalizado.html')

@orders_bp.route('/mis-pedidos')
@login_required
def mis_pedidos():
    """Ver mis pedidos"""
    usuario_id = session['usuario_id']
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pedidos WHERE usuario_id = %s ORDER BY fecha_pedido DESC', (usuario_id,))
        pedidos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('mis-pedidos.html', pedidos=pedidos)
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return render_template('mis-pedidos.html', pedidos=[])

@orders_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Completar compra"""
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
        
        if request.method == 'POST':
            if not items:
                flash('El carrito está vacío', 'warning')
                cursor.close()
                conn.close()
                return redirect(url_for('main.carrito'))
            
            total = sum(item['precio'] * item['cantidad'] for item in items)
            
            # Crear pedidos
            for item in items:
                cursor.execute("""
                    INSERT INTO pedidos (usuario_id, tipo_flor, cantidad, total, estado)
                    VALUES (%s, %s, %s, %s, 'confirmado')
                """, (usuario_id, item['nombre'], item['cantidad'], item['precio'] * item['cantidad']))
            
            # Limpiar carrito
            cursor.execute('DELETE FROM carrito WHERE usuario_id = %s', (usuario_id,))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            flash('¡Compra realizada exitosamente!', 'success')
            return redirect(url_for('orders.mis_pedidos'))
        
        # GET
        total = sum(item['precio'] * item['cantidad'] for item in items) if items else 0
        cursor.close()
        conn.close()
        return render_template('checkout.html', items=items, total=total)
    
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return render_template('checkout.html', items=[], total=0)
