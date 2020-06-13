import sys, os
import time
import random
from colorama import *

init()

color = [Fore.RED, Fore.WHITE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
fondo = [Back.RED, Back.BLUE, Back.GREEN, Back.YELLOW, Back.WHITE]

saludo = "Bienvenido"
var2 = 11 * "_"

os.system("title Hola && cls")

def tiempo(t = 0.04):
	time.sleep(t)

def nota():
	aNoTando = ("\n\n anotando")
	cargando = ("....")
	for i in aNoTando:
		tiempo(0.06)
		print(random.choice([Fore.RED, Fore.WHITE])+i, end="")

	for j in cargando:
		tiempo(0.25)
		print((Fore.MAGENTA)+j, end="")

def margen(t = 0.08):
	print("   ", end="")
	for i in var2:
		print(random.choice(color)+" "+i, end="")
		#sys.stdout.flush()
		tiempo(t)
	print("\n")

def bienvenido(t = 0.08):
	print("   |", end="")
	print(Fore.RESET,end=" ")
	for i in saludo:
		tiempo(t)
		print(random.choice(color)+i, end=" ")
		#sys.stdout.flush()
	print("|")

def genero():
	varGenero = "\n ¿Cual es tu Genero?\n\n 1) Hombre\n 2) Mujer"
	for i in varGenero:
		tiempo()
		print(random.choice(color)+i, end="")

	# Validacion para solo numeros
	while True:
		NoUnoOdos = ("\n Escoge 1 o 2 segun tu respuesta:\n"+varGenero)
		try:
			ResPuesta = int(input("\n\n>> "))
			if(ResPuesta < 1 or ResPuesta > 2):
				for j in NoUnoOdos:
					tiempo(0.03)
					print(random.choice(color)+j, end="")
				pass
			else:
				break
		except:
			soloNum = ("\n Solo se permiten Numeros\n"+NoUnoOdos)
			for i in soloNum:
				tiempo(0.03)
				print(random.choice(color)+i, end="")
			pass

	global genero
	# Validacion de respuesta
	if(ResPuesta == 1):
		masculino = "\n ¡Bien! Eres Hombre"
		genero = "Hombre"
		for i in masculino:
			tiempo()
			print(random.choice(color)+i, end="")
	elif(ResPuesta == 2):
		femenino = "\n ¡Bien! Eres Mujer"
		genero = "Mujer"
		for i in femenino:
			tiempo()
			print(random.choice(color)+i, end="")

	tiempo(0.80)
	print("\n\n")
	nota()


def person():
	persona = "\n\n ¿Quien eres?"
	saludo = " Hola "
	for i in persona:
		tiempo()
		print(random.choice(color)+i, end="")
	print("\n")
	ResPuesta = input(">> ")

	# Guardar el Nombre Ingresado
	global nombre
	nombre = ResPuesta

	print("\n")
	for x in saludo:
		tiempo()
		print(random.choice(color)+x, end="")
	for j in ResPuesta:
		tiempo()
		print(random.choice(color)+j, end="")
	print("\n"*4)
	nota()


def funEstado():
	varEstado = ("\n\n ¿Como estas "+ nombre +"? \n\n 1) Bien\n 2) Mal")
	respuesta = ("\n 1) Bien\n 2) Mal")

	for i in varEstado:
		tiempo()
		print(random.choice(color)+i, end="")
		
	# Validacion para solo numeros
	while True:
		NoUnoOdos = ("\n Escoge 1 o 2 segun tu respuesta: "+respuesta)
		try:
			ResPuesta = int(input("\n\n>> "))
			if(ResPuesta < 1 or ResPuesta > 2):
				for j in NoUnoOdos:
					tiempo(0.04)
					print(random.choice(color)+j, end="")
				pass
			else:
				break
		except:
			soloNum = ("\n Solo se permiten Numeros\n"+NoUnoOdos)
			for i in soloNum:
				tiempo(0.04)
				print(random.choice(color)+i, end="")
			pass

	global estado
	# Validacion de respuesta
	if(ResPuesta == 1):
		bien = "\n ¡GENIAL!"
		estado = "Bien"
		for i in bien:
			tiempo()
			print(random.choice(color)+i, end="")
	elif(ResPuesta == 2):
		mal = "\n QUE MAL :("
		estado = "Mal"
		for i in mal:
			tiempo()
			print(random.choice(color)+i, end="")
	tiempo(0.80)
	print("\n")
	nota()


def gustos():

	preGustos = ("\n\n  ¿Que Deporte te gusta?")
	cosas = ("\n\n  1) Futbol\t2) BallquetBall\n  3) Boleibol\t4) Skate")

	for i in preGustos:
		tiempo(0.07)
		sys.stdout.flush()
		print(random.choice(color)+i, end="")

	for j in cosas:
		tiempo(0.04)
		print(random.choice(color)+j, end="")

	# Validacion para solo numeros
	while True:
		try:
			ResPuesta = int(input("\n\n>> "))
			if(ResPuesta < 1 or ResPuesta > 4):
				NoUnoOdos = ("\n Escoge 1 a 4 segun tu respuesta: "+cosas)
				for j in NoUnoOdos:
					tiempo(0.04)
					print(random.choice(color)+j, end="")
				pass
			else:
				break
		except:
			soloNum = ("\n Solo se permiten Numeros\n"+NoUnoOdos)
			for i in soloNum:
				tiempo(0.04)
				print(random.choice(color)+i, end="")
			pass

	def estadoBien():
		bien = "\n ¡BIEN!"
		for i in bien:
			tiempo()
			print(random.choice(color)+i, end="")

	global gusto
	# Validacion de respuesta y Guardar gusto
	if(ResPuesta == 1 or ResPuesta == 2 or ResPuesta == 3):
		estadoBien()
		gusto = "Futbol"
	elif(ResPuesta == 2):
		estadoBien()
		gusto = "BallquetBall"
	elif(ResPuesta == 3):
		estadoBien()
		gusto = "Boleibol"
	elif(ResPuesta == 4):
		mal = "\n A MI Igual :D\n\n ¡GENIAL!"
		for i in mal:
			tiempo()
			print(random.choice(color)+i, end="")
		gusto = "Skate"

	tiempo(0.80)
	print("\n\n")
	nota()

numPregunta = 1
done = True
while done:
	t = 0.08

	if(numPregunta > 1):
		t = 0

	print("\n")
	margen(t)
	bienvenido(t)
	margen(t)

	if(numPregunta == 1):
		genero()
		os.system("cls")
		numPregunta += 1
	elif(numPregunta == 2):
		person()
		os.system("cls")
		numPregunta += 1
	elif(numPregunta == 3):
		funEstado()
		os.system("cls")
		numPregunta += 1
	elif(numPregunta == 4):
		gustos()
		os.system("cls")
		done = False

def titleDatos():
	varDatos = "\n   | DATOS INGRESADOS |"
	NumeroMargen = "-" * 18

	def margenDatos():
		print("\n    ", end="")
		for i in NumeroMargen:
			tiempo(0.03)
			print(random.choice(color)+i, end="")

	margenDatos()
	for i in varDatos:
		tiempo()
		print(random.choice(color)+i, end="")

	margenDatos()
	print("\n\n")

def Datos():
	elGenero = (" Genero: "+ genero +"\n\n")
	elNombre = (" Tu Nombre es: "+ nombre +"\n\n")
	elEstado = (" Te encuentras: "+ estado +"\n\n")
	elGusto = (" Te Gusta: El "+ gusto +"\n\n")

	for j in elGenero:
		tiempo(0.064)
		print(random.choice(color)+j, end="")

	for i in elNombre:
		tiempo(0.064)
		print(random.choice(color)+i, end="")

	for x in elEstado:
		tiempo(0.064)
		print(random.choice(color)+x, end="")

	for e in elGusto:
		tiempo(0.064)
		print(random.choice(color)+e, end="")


titleDatos()
Datos()


tiempo(3)

os.system("cls")
os.system("color 02")