#Importo librerias
from gpiozero import PWMLED
import time
import ADS1x15
from math import log

#Declaro variables para el cálculo de temperatura medida por el voltaje de ADC
Beta = 3950
Temp_Inicial = 298
R1 = 10000
Vref = 3.3

#Leds configurados en PWM
ledR = PWMLED(19)
ledB = PWMLED(26)

#Funciones para el uso de ADC
ADS = ADS1x15.ADS1115(1,0X48)
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()


while True :
	#Leo los valores raw medidos del potenciometro y el termistor
	val_pot = ADS.readADC(3)
	val_ntc = ADS.readADC(1)

	#Convierto los valores raw en valores de voltaje
	volt_ntc = val_ntc * f
	volt_pot = val_pot * f

	#Calculo la resistencia del termistor con divisor de tensión para el cálculo de la temperatura medida
	res_ntc = R1 / ( Vref / volt_ntc  - 1 )
	print(res_ntc)

	#Calculo la temperatura segun el valor de resistencia del termistor (ecuacion)
	temp_ntc = (Beta / (log(res_ntc / R1) + (Beta / Temp_Inicial)) - 273)
	print (temp_ntc)
	#Calculo temperatura equivalente del potenciometro - Como se el comportamiento del potenciometro en cada uno de sus
	#extremos y cada extremo tiene su equivalente en grados (0° a 30°), la trabajo como ecuación lineal
	#y = (30°/3.3V)*x + 30
	temp_pot = (30/(-3.3))*volt_pot +  30
	print (temp_pot)

	# Veo si la temperatura del termistor es mayor o menor (si es la misma apago ambos)
	if(temp_ntc > temp_pot):
		#Si la del termistor es mayor que la del pot, enciendo solo la luz azul
		temp_dif = temp_ntc - temp_pot
		print (temp_dif)
		ledR.value = 0
		if (temp_dif > 5):
			ledB.value = 1
		else:
			ledB.value = temp_dif / 5
	elif (temp_ntc < temp_pot):
		#Si la del termistor es menor que la del pot, enciendo solo la luz roja
		temp_dif = temp_pot - temp_ntc
		print (temp_dif)
		ledB.value = 0
		if (temp_dif > 5):
			ledR.value = 1
		else:
			ledR.value = temp_dif / 5
	else:
		ledR.value = 0
		ledB.value = 0

	#Muestro ambos resultados para comparar
	print (temp_ntc)
	print (temp_pot)
	time.sleep(1)
