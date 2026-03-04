import time
import pyautogui

time.sleep(5) # Aguarda 5 segundos para o usuário posicionar o mouse no local desejado
print(pyautogui.position())# Retorna a posição atual do mouse na tela, útil para identificar as coordenadas para clicar em elementos específicos.