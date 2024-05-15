import sys
from gpiozero import LED, Buzzer
from time import sleep
#Importo librerias necesarias

ledR = LED (19)
ledG = LED (13)
ledB = LED (26)
bz = Buzzer (22)
# GPIO declarados

comandos = ["BUZZER ON", "BUZZER OFF", "RGB BLUE","RGB RED", "RGB BLUE"]

while True:
	print ("Ingrese comando con formato: [COMANDO] [OPCION]. Ejemplo: BUZZER ON.")
	print ("Ingrese HELP para una lista completa de comandos ingresables")
	answer = sys.stdin.readline()
	if answer == "HELP\n":
		print (*comandos, sep = "\n")
    # User command stored in answer for the ifs - The help command resets the loop
	elif answer == "BUZZER ON\n":
		bz.on()
	elif answer == "BUZZER OFF\n":
		bz.off()
    # Estados de los buzzer
	elif answer == "RGB BLUE\n":
		if ledB.value == 0:
			ledB.on()
		else:
			ledB.off()
    # Cambio de estado del led azul
	elif answer == "RGB RED\n":
		if ledR.value == 0:
			ledR.on()
		else:
			ledR.off()
    # Cambio de estado del led azul
	elif answer == "RGB GREEN\n":
		if ledB.value == 0:
			ledG.on()
		else:
			ledG.off()
    # Cambio de estado del led ver
