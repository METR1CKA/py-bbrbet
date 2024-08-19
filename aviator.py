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


# Función para decidir si se genera una "Apuesta 2"
def decidir_apuesta_2(multiplicador, apuesta_1):
    if multiplicador > 4 or (multiplicador <= 4 and apuesta_1 > 10):
        return True
    else:
        return np.random.choice([True, False])


# Función para calcular "Apuesta 2" y "Multiplicador 2" según las condiciones finales
def calcular_apuesta_2_y_multiplicador_2_para_recuperacion(apuesta_1):
    apuesta_2 = apuesta_1 // 2
    multiplicador_2 = (apuesta_1 + apuesta_2) / apuesta_2
    return multiplicador_2, apuesta_2


# Ejecutar 10 veces y almacenar resultados
resultados = []
for _ in range(10):
    multiplicador = obtener_multiplicador()
    apuesta_1 = obtener_apuesta_modificada(multiplicador)
    if decidir_apuesta_2(multiplicador, apuesta_1):
        multiplicador_2, apuesta_2 = (
            calcular_apuesta_2_y_multiplicador_2_para_recuperacion(apuesta_1)
        )
    else:
        multiplicador_2, apuesta_2 = None, None
    resultados.append((multiplicador, apuesta_1, multiplicador_2, apuesta_2))

# Imprimir resultados
for i, (multiplicador, apuesta_1, multiplicador_2, apuesta_2) in enumerate(
    resultados, 1
):
    print(
        f"\nEjecución {i}:\nMultiplicador 1: {multiplicador} - Apuesta 1: {apuesta_1}\nMultiplicador 2: {multiplicador_2} - Apuesta 2: {apuesta_2}"
    )
