import pyautogui as pa
from time import sleep

while True:
    i = int(input("    :"))
    while True:
        if i == 0 :
            fice = list(pa.center(pa.locateOnScreen("1.PNG")))
            pa.click(fice)
            sleep(3)
            i += 1
            continue
        j = 140
        while j >0:
            print("남은 시간 : %02d: %02d"%(j//60, j-(j//60)*60), end='\r')
            sleep(1)
            j -= 1
        try:
            lace = list(pa.center(pa.locateOnScreen("2.PNG")))
            pa.click(lace)
            pa.move(100,100)

            try:
                center3 = pa.locateOnScreen("3.PNG")
                sleep(1)
                pa.press('enter')

            except:
                break

        except:
            try:
                center4 = list(pa.center(pa.locateOnScreen("4.PNG")))
                pa.click(center4)
                pa.move(100,100)
                sleep(1)
                pa.press('enter')
            except:
                break
