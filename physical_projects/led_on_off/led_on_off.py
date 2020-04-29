# connect long leg of LED to GPIO 17, with 50ohm resistor 
# connect short leg to GND


from gpiozero import LED
from time import sleep 


led = LED(17) 

while True: 
	led.on()
	sleep(1)
	led.off()
	sleep(1)

# if you connect the long leg to 3V3, the LED will always be on
# with GPIO 17, you can control on/off with the code