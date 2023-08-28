import time

def main():
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    
    tiempo_limite = horas * 3600 + minutos * 60 + segundos
    
    print("\nCronómetro iniciado:")
    tiempo_actual = 0
    
    while tiempo_actual < tiempo_limite:
        horas_actual = tiempo_actual // 3600
        minutos_actual = (tiempo_actual % 3600) // 60
        segundos_actual = tiempo_actual % 60
        
        print(f"{horas_actual:02d}:{minutos_actual:02d}:{segundos_actual:02d}", end="\r")
        time.sleep(1)
        
        tiempo_actual += 1
    
    print("\nTiempo límite alcanzado.")

if __name__ == "__main__":
    main()
