#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inicializador de blueprints
"""

from .auth import auth_bp
from .main import main_bp
from .orders import orders_bp

__all__ = ['auth_bp', 'main_bp', 'orders_bp']
