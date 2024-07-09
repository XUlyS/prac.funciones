#areas.py

import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

def area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2
