#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funciones utilitarias para la aplicación
"""

import os
from flask import url_for, current_app

def inject_helpers():
    """Context processor para inyectar funciones útiles en plantillas"""
    
    def image_url(filename):
        """
        Devuelve la URL correcta de una imagen.
        Busca primero en static/images, luego en images/
        """
        if not filename:
            return url_for('static', filename='images/sunflower.svg')
        
        static_path = os.path.join(current_app.root_path, 'static', 'images', filename)
        if os.path.exists(static_path):
            return url_for('static', filename='images/' + filename)
        
        images_path = os.path.join(current_app.root_path, 'images', filename)
        if os.path.exists(images_path):
            return url_for('main.serve_image', filename=filename)
        
        # Mapeos conocidos entre nombres en BD y archivos reales
        mapping = {
            'sunflower.jpg': 'Girasol_Eterno.jpg',
            'tulip.jpg': 'Tulipan_Eterno.jpg',
            'rose.jpg': 'Rosas_Eternas.jpg',
            'single1.jpg': 'Flor_Unica.jpg',
            'single2.jpg': 'Flor_Unica_2jpg.jpg',
            'single3.jpg': 'Flor_Unica_3.jpg',
            'Ramo-Clasico.jpg': 'Ramo-Clasico.jpg',
            'Ramo-Moderno.jpg': 'Ramo_Moderno.jpg',
            'Ramo-Deluxe.jpg': 'Ramo_Deluxe.jpg',
        }
        
        alt = mapping.get(filename)
        if alt and os.path.exists(os.path.join(current_app.root_path, 'images', alt)):
            return url_for('main.serve_image', filename=alt)
        
        return url_for('static', filename='images/sunflower.svg')
    
    return dict(image_url=image_url)
