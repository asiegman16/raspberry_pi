from gpiozero import LED, Button
from time import sleep

led = LED(17) 
button - Button(2)

while True: 
	button.wait_for_press()
	led.toggle() # switches state of LED from on to off, or off to on
	sleep(0.5) 