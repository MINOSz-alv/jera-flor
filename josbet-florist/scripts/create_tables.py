#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear las tablas sin dropear la BD existente
"""

import mysql.connector
from mysql.connector import Error

def crear_tablas():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='floreria_josbet',
            autocommit=True
        )
        cursor = conn.cursor()
        
        # Tabla de usuarios
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    correo VARCHAR(100) UNIQUE NOT NULL,
                    contrasena VARCHAR(255) NOT NULL,
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("✓ Tabla 'usuarios' creada")
        except Error as e:
            if "already exists" in str(e):
                print("⚠ Tabla 'usuarios' ya existe")
            else:
                raise
        
        # Tabla de productos
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT,
                    precio DECIMAL(10, 2) NOT NULL,
                    imagen VARCHAR(255),
                    categoria VARCHAR(50)
                )
            """)
            print("✓ Tabla 'productos' creada")
        except Error as e:
            if "already exists" in str(e):
                print("⚠ Tabla 'productos' ya existe")
            else:
                raise
        
        # Tabla de pedidos
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    tipo_flor VARCHAR(100),
                    color VARCHAR(50),
                    cantidad INT DEFAULT 1,
                    mensaje TEXT,
                    extra_kit VARCHAR(50),
                    extra TEXT,
                    total DECIMAL(10, 2),
                    estado VARCHAR(20) DEFAULT 'pendiente',
                    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
                )
            """)
            print("✓ Tabla 'pedidos' creada")
        except Error as e:
            if "already exists" in str(e):
                print("⚠ Tabla 'pedidos' ya existe")
            else:
                raise
        
        # Tabla de carrito
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS carrito (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    usuario_id INT NOT NULL,
                    producto_id INT NOT NULL,
                    cantidad INT DEFAULT 1,
                    fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
                    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
                )
            """)
            print("✓ Tabla 'carrito' creada")
        except Error as e:
            if "already exists" in str(e):
                print("⚠ Tabla 'carrito' ya existe")
            else:
                raise
        
        # Insertar productos si no existen
        cursor.execute("SELECT COUNT(*) FROM productos")
        count = cursor.fetchone()[0]
        
        if count == 0:
            print("\nInsertando productos...")
            productos = [
                ('Girasol eterno', 'Hermoso girasol de flores eternas', 25.99, 'Girasol_Eterno.jpg', 'flores'),
                ('Tulipanes eternos', 'Ramo de tulipanes eternos variados', 35.99, 'Tulipan_Eterno.jpg', 'flores'),
                ('Rosas eternas', 'Ramo de rosas rojas eternales', 45.99, 'Rosas_Eternas.jpg', 'flores'),
                ('Flor única 1', 'Flor exótica única', 15.99, 'Flor_Unica.jpg', 'individual'),
                ('Flor única 2', 'Flor decorativa especial', 18.99, 'Flor_Unica_2jpg.jpg', 'individual'),
                ('Flor única 3', 'Flor elegante y moderna', 20.99, 'Flor_Unica_3.jpg', 'individual'),
                ('Ramo clásico', 'Ramo tradicional de flores mixtas', 39.99, 'Ramo-Clasico.jpg', 'ramos'),
                ('Ramo moderno', 'Ramo con diseño contemporáneo', 49.99, 'Ramo_Moderno.jpg', 'ramos'),
                ('Ramo deluxe', 'Ramo premium con flores premium', 69.99, 'Ramo_Deluxe.jpg', 'ramos'),
            ]
            
            cursor.executemany(
                "INSERT INTO productos (nombre, descripcion, precio, imagen, categoria) VALUES (%s, %s, %s, %s, %s)",
                productos
            )
            print(f"✓ {cursor.rowcount} productos insertados")
        else:
            print(f"⚠ La tabla 'productos' ya tiene {count} registros")
        
        cursor.close()
        conn.close()
        
        print("\n✅ Base de datos lista!")
        
    except Error as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == '__main__':
    crear_tablas()
