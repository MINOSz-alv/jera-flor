#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Factory de la aplicación Flask para Florería Josbet
"""

from flask import Flask
from config import config

def create_app(config_name='development'):
    """Factory para crear la aplicación Flask"""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Registrar blueprints
    from app.routes import auth_bp, main_bp, orders_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(orders_bp)
    
    # Context processors
    from app.utils import inject_helpers
    app.context_processor(inject_helpers)
    
    # Manejadores de errores
    @app.errorhandler(404)
    def not_found(error):
        from flask import render_template
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def server_error(error):
        from flask import render_template
        return render_template('500.html'), 500
    
    return app
