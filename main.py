from machine import Pin,ADC
from time import sleep
from math import log

led = Pin(25, Pin.OUT)
adc = ADC(26)

while True:
  lect = adc.read_u16()
  print("Valor del ADC: {}".format(lect))
  Vout = 3.3/65535*lect
  print("Valor de Tensión: {}".format(Vout))
  R1 = 10000
  R2 = (Vout*R1)/(3.3-Vout)
  BETA = 3950
  print("Valor de R2: {}".format(R2))
  temperatura = (BETA / (log(R2/R1)+BETA/298))-273
  print("Temperatura: {}".format(temperatura))
  sleep(0.5)
