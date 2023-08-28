import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
         os.system('cls')
         print("***Cronometro :D ***")
         print(f'{hora:02d}:{minuto:02d}:{segundo:02d}')
         time.sleep(1)

