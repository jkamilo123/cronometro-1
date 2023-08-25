import os
import time

def Opc1():
    for hora in range(24):
        for minuto in range(60):
            for segundo in range(60):
             os.system('cls')
             print("***Cronometro :D ***")
             print(f'{hora}:{minuto}:{segundo}')
             time.sleep(1)


def Opc2():
        input("Ingrese la hora ")
        input("Ingrese el minuto ")
        input("Ingrese los segundos ")
        h = int()
        m = int()
        s = int()

        for hora in range(h):
            for minuto in range(m):
                for segundo in range(s):
                    os.system('cls')
                    print(f'{hora}:{minuto}:{segundo}')
                    time.sleep(1)

print("***Cronometro :D ***")
print("1. Cronometro normal")
print("2. configurar cronometro")
c = input("Ingrese una opcion ")
if c=="1":
   Opc1()
elif c=="2":
   Opc2() 
   
