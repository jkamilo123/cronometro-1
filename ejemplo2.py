
import time

# Solicitar al usuario ingresar el tiempo límite en horas, minutos y segundos
horas_limite = int(input("Ingrese las horas límite: "))
minutos_limite = int(input("Ingrese los minutos límite: "))
segundos_limite = int(input("Ingrese los segundos límite: "))

# Convertir el tiempo límite a segundos totales
limite_en_segundos = horas_limite * 3600 + minutos_limite * 60 + segundos_limite

# Cronometrar y mostrar el tiempo hasta llegar al límite
for tiempo_actual in range(limite_en_segundos + 1):
    horas_actual = tiempo_actual // 3600
    minutos_actual = (tiempo_actual % 3600) // 60
    segundos_actual = tiempo_actual % 60
    print(f"{horas_actual:02d}:{minutos_actual:02d}:{segundos_actual:02d}", end="\r")
    time.sleep(1)

print("\n¡Tiempo límite alcanzado!")

