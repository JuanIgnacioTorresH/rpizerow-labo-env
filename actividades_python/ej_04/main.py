from gpiozero import MCP3008, PWMLED
import time
import ADS1x15

NTC = 10000
R1 = 10000
Beta = 3950
Temp_inicial = 298

ledR = PWMLED(19)
ledB = PWMLED(26)
ADS = ADS1x15.ADS1115(1,0X48)
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

while True :
	val_pot = ADS.readADC(3)
	val_ntc = ADS.readADC(1)
	volt_ntc = val_ntc * f
	volt_pot = val_pot * f
	ntc_res = R1 / ( Vref / volt_ntc - 1 ) 
	temp_ntc = Beta / (log(NTC / R1) + (Beta / Temp_Inicial))
	temp_pot = (volt_ntc * 30) / 10000
	if(volt_ntc < volt_pot):
		ledB.on()
	else:
		ledR.on()
	print (volt_ntc)
	print (volt_pot)
	time.sleep(1)
