# Uso del paquete geometria# Autor: Danilo
# Fecha: 8 de julio de 2024
# Versión: 1
from geometria import area_circulo, area_rectangulo, area_triangulo

print(area_circulo(5))
print(area_rectangulo(4, 6))
print(area_triangulo(3, 7))

# Uso del paquete analisis_texto
from analisis_texto import contar_palabras, contar_frecuencia_palabras, reemplazar_palabra

texto = "hola mundo hola python"
print(contar_palabras(texto))
print(contar_frecuencia_palabras(texto))
print(reemplazar_palabra(texto, "hola", "adios"))
