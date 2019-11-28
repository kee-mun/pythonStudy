import pyautogui as pa
from time import sleep

while True:
    cli = int(input("반복 횟수:"))
    i = 0

    while i< cli:
        temp = list(pa.position())

        pa.click(temp[0],temp[1])
        print("%02d 번째 반복중"%(i+1),end='\r')

        sleep(3)
        
        i += 1
    print("")
    pa.press('enter')
