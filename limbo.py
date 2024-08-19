import numpy as np


# Configuramos la semilla para reproducibilidad (opcional)
np.random.seed(0)


# Función para obtener un multiplicador con una distribución exponencial invertida
def obtener_multiplicador(minimo=1.20, maximo=30.0, factor=1.0):
    multiplicador = maximo - (np.random.exponential(scale=factor) * (maximo - minimo))
    return max(minimo, multiplicador)


# Función para obtener la "Apuesta 1" modificada, con menor impacto del multiplicador
def obtener_apuesta_modificada(
    multiplicador, minimo=1, maximo=20, factor_influencia=0.5
):
    apuesta = maximo - (
        (multiplicador - 1.20) / (30.0 - 1.20) * (maximo - minimo) * factor_influencia
    )
    return max(minimo, round(apuesta))


# Ejecutar 10 veces y almacenar resultados
resultados = []
for _ in range(10):
    multiplicador = obtener_multiplicador()
    apuesta_1 = obtener_apuesta_modificada(multiplicador)
    resultados.append((multiplicador, apuesta_1))

# Imprimir resultados
for i, (multiplicador, apuesta_1) in enumerate(resultados, 1):
    print(f"\nEjecución {i}: Multiplicador 1: {multiplicador} - Apuesta 1: {apuesta_1}")
