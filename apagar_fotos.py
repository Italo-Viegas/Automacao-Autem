import pyautogui as pa
import time
pa.PAUSE = 1.5
# ir para o chrome
pa.hotkey('alt', 'tab')


while True:

# abrir o checklist x=365, y=166
    pa.click(365, 166)
    time.sleep(2)
# abrir as fotos x=524, y=413
    pa.click(524, 413)
# apagar as fotos x=1463, y=816 / x=1115, y=611
    pa.click(1523, 823)
    pa.click(1115, 611)
    time.sleep(1)
    pa.click(1523 ,823)
    pa.click(1115, 611)
    time.sleep(1)
    pa.click(1523, 823)
    pa.click(1115, 611)
    time.sleep(1)
    pa.click(1523 ,823)
    pa.click(1115, 611)
    time.sleep(1)
    pa.click(1523, 823)
    pa.click(1115, 611)
    time.sleep(1)
    pa.click(1523, 823)
    pa.click(1115, 611)

   
# voltar para o checklist 1066, y=1047 /x=979, y=923
    pa.click(1066, 1047)
    pa.click(979, 923)
# scrollar para baixo 
    pa.scroll(-42)
