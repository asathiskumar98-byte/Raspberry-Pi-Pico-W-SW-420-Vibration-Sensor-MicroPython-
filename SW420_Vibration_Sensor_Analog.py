import machine
from machine import ADC
import time

SW420 = ADC(0)

while True:
    adc_value = SW420.read_u16()  # 0 - 65535
    print('SW420 Vibration Value:',adc_value)
    time.sleep(0.2)
