from gpiozero import Button, LED

button = Button(21) 
led = LED(25)

while True: 
	button.wait_for_press()
	led.on() # or, led.blink() or, led.blink(2,2) which means 2 seconds on, 2 seconds off
	button.wait_for_release()
	led.off()


# /// # /// # /// BELOW IS FULL TRAFFIC LIGHT CODE # /// # /// # ///

"""from gpiozero import Button, TrafficLights, Buzzer
from time import sleep 

lights = TrafficLights(25,8,7)
buzzer = Buzzer(15)

while True: 
	button.wait_for_press()
	lights.green.on()
	sleep(1)
	lights.amber.on()
	sleep(1)
	lights.red.on()
	sleep(1)
	lights.off()"""
	

