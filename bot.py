#Bibliotecas
from pyautogui import locateOnScreen
from time import sleep
import win32api as wapi
import sys

#Arquivos
from mudar_de_sala import mudar_de_sala
from comando import comando

while(True):
    img_controle = locateOnScreen('Screenshot_1.PNG', confidence = 0.7)

    if img_controle:
        mudar_de_sala()
        img_controle = None
        sleep(5)

    if 'P' in comando(): 
    	mudar_de_sala()

    if 'O' in comando():
    	exit() 