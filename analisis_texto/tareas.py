# tareas.py

from collections import Counter

def contar_palabras(texto):
    """Cuenta la cantidad de palabras en una cadena de texto."""
    palabras = texto.split()
    return len(palabras)

def contar_frecuencia_palabras(texto):
    """Cuenta la cantidad de veces que aparece cada palabra en una cadena de texto."""
    palabras = texto.split()
    frecuencia = Counter(palabras)
    return frecuencia

def reemplazar_palabra(texto, palabra_vieja, palabra_nueva):
    """Reemplaza una palabra por otra en una cadena de texto."""
    return texto.replace(palabra_vieja, palabra_nueva)
