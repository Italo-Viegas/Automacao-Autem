#09.460.158/0001-19
import pyautogui as pa
import time
pa.PAUSE = 1.5
#ir para o chrome
pa.hotkey('alt', 'tab')


while True:

    #abrir o checklist x=365, y=166
    pa.click(94, 120)
    pa.scroll(-42)
    #abrir as fotos x=524, y=413
    pa.click(483 ,413)
    pa.scroll(-807)
    #apagar as fotos x=1463, y=816 / x=1115, y=611
    pa.click(666, 512)
    pa.click(938 ,414)
    time.sleep(1)
    pa.click(667, 510)
    pa.click(938 ,414)
    time.sleep(1)
    pa.click(667, 510)
    pa.click(938 ,414)
    time.sleep(1)
    pa.click(667, 510)
    pa.click(938 ,414)
