#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para insertar datos de prueba en la BD
"""

import mysql.connector
from mysql.connector import Error

def insertar_datos_prueba():
    try:
        # Conectar a MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='floreria_josbet',
            autocommit=True
        )
        cursor = conn.cursor()
        
        # Insertar usuarios
        print("Insertando usuarios de prueba...")
        usuarios = [
            ('Karen Flores', 'karen@example.com', '12345'),
            ('Juan Pérez', 'juan@example.com', '12345'),
            ('María García', 'maria@example.com', '12345'),
        ]
        
        for nombre, correo, contrasena in usuarios:
            try:
                cursor.execute(
                    'INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)',
                    (nombre, correo, contrasena)
                )
                print(f"✓ Usuario '{nombre}' creado")
            except Error as e:
                if "Duplicate entry" in str(e):
                    print(f"⚠ Usuario '{nombre}' ya existe")
                else:
                    print(f"✗ Error: {e}")
        
        # Insertar productos
        print("\nInsertando productos...")
        productos = [
            ('Ramo Clásico', 'Hermoso ramo de rosas rojas', 45.99, 'Ramo-Clasico.jpg'),
            ('Ramo Moderno', 'Arreglo floral moderno y elegante', 55.99, 'Ramo-Moderno.jpg'),
            ('Ramo Deluxe', 'Colección premium de flores frescas', 75.99, 'Ramo-Deluxe.jpg'),
            ('Girasol Eterno', 'Flor singular de girasol preservado', 25.99, 'Girasol_Eterno.jpg'),
            ('Tulipán Eterno', 'Tulipanes preservados en caja', 35.99, 'Tulipan_Eterno.jpg'),
            ('Rosas Eternas', 'Docena de rosas preservadas', 65.99, 'Rosas_Eternas.jpg'),
        ]
        
        for nombre, descripcion, precio, imagen in productos:
            try:
                cursor.execute(
                    'INSERT INTO productos (nombre, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)',
                    (nombre, descripcion, precio, imagen)
                )
                print(f"✓ Producto '{nombre}' creado - ${precio}")
            except Error as e:
                if "Duplicate entry" in str(e):
                    print(f"⚠ Producto '{nombre}' ya existe")
                else:
                    print(f"✗ Error: {e}")
        
        cursor.close()
        conn.close()
        
        print("\n✅ Datos de prueba insertados exitosamente!")
        print("\nPuedes iniciar sesión con:")
        print("  📧 Correo: karen@example.com")
        print("  🔐 Contraseña: 12345")
        
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        print("\n💡 Asegúrate de que:")
        print("  1. MySQL está ejecutándose en XAMPP")
        print("  2. La BD 'floreria_josbet' existe")
        print("  3. Las credenciales en .env son correctas")

if __name__ == '__main__':
    insertar_datos_prueba()
