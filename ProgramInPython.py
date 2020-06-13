import sys, os
import time
import random
from colorama import *

# modulo colorama python 3

# for import module
# from colorama import init, Fore, Back, Style

# Estilos   | (Style)
# Debil     | DIM
# Normal    | NORMAL
# Brillante | BRIGHT
# Reset     | RESET_ALL


# Colores Texto/Fondo | (Fore/Back)
# Negro				  | BLACK
# Rojo				  | RED
# Verde				  | GREEN
# Amarillo 			  | YELLOW
# Azul 				  | BLUE
# Morado			  | MAGENTA
# Cian				  | CYAN
# Blanco 			  | WHITE
# Reset 			  | RESET

init()

color = [Fore.RED, Fore.WHITE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
fondo = [Back.RED, Back.BLUE, Back.GREEN, Back.YELLOW, Back.WHITE]

saludo = "Programando en Python"
var2 = 22 * "_"

os.system("cls")
print("\n")

def tiempo(t = 0.04):
	time.sleep(t)

def margen():
	print("\t", end="")
	for i in var2:
		print(random.choice(color)+" "+i, end="")
		#sys.stdout.flush()
		tiempo()
	print("\n")

def Programando():
	margen()
	print("\t|", end="")
	print(Fore.RESET,end=" ")
	for i in saludo:
		tiempo()
		print(random.choice(color)+i, end=" ")
		#sys.stdout.flush()
	print("|")
	margen()
	tiempo(3)

Programando()