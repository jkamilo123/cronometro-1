import time

def cronometro(tiempo_total):
    tiempo_inicial = time.time()
    tiempo_final = tiempo_inicial + tiempo_total
    
    while time.time() < tiempo_final:
        tiempo_transcurrido = int(time.time() - tiempo_inicial)
        horas, segundos_restantes = divmod(tiempo_transcurrido, 3600)
        minutos, segundos = divmod(segundos_restantes, 60)
        
        print(f"Tiempo transcurrido: {horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)
    
    print("\n¡Tiempo indicado alcanzado!")

tiempo_indicado = int(input("Ingresa el tiempo en segundos para el cronómetro: "))
cronometro(tiempo_indicado)
