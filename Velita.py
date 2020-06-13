import sys
import os
import time
from colorama import *

init()

os.system("title Velita && cls")


var = Fore.WHITE + "\n\tHoy 7/12/2017 es el dia de las velitas"
for i in var:
	time.sleep(0.03)
	print(i, end="")



def DatoYpregunta():
	querer = Fore.BLACK+Back.RED + "\n\n\t¿Quieres encender una Velita?" + Style.RESET_ALL
	textRespuesta = Fore.RED + "\n\n\t> Si(Y)\n\t> No(N)"
	for i in querer:
		time.sleep(0.03)
		print(i, end="")
	print(textRespuesta)



done = True
while done:
	DatoYpregunta()
	respuesta = input(str("\n\t >> "))
	if(respuesta != "y"):
		os.system("cls")
	elif(respuesta == "y"):
		done = False
		os.system("cls")




def estadoVela():

	color = Fore.BLACK

	done2 = True
	while done2:
		
		print()

		# Velita /////////////////////////////////////
		print(color)
		print("\t\t          ")
		print("\t\t    /\    ")
		print("\t\t   /  \   ")
		print("\t\t  / /\ \  ")
		print("\t\t  \ \/ /  ")
		print("\t\t   \  /   ")
		print("\t\t    \/    ")
		x = "|"
		print(Fore.WHITE+"\t\t |------| ")

		for i in range(8):
			print("\t\t "+ x +"      "+x+" ")

		print("\t\t "+ x +"______"+x+" "+"\n\t\t          "+Style.RESET_ALL)

		# ////////////////////////////////////////////
		

		ONVelita = Fore.CYAN + "   • Para Encender Oprimir la tecla [y] y dar ENTER"
		OFFVelita = Fore.YELLOW + "   • Para  Apagar  Oprimir la tecla [N] y dar ENTER"

		print("\n\n"+ ONVelita +"\n"+ OFFVelita)
		print("\n")

		respuesta = input(str("\t >> "))

		print(Fore.RESET)
		
		if(respuesta == "y"):
			color = Fore.YELLOW

		elif(respuesta == "n"):
			color = Fore.BLACK

		os.system("cls")



estadoVela()