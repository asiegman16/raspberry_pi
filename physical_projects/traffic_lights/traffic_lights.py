"""from gpiozero import Button, LED

button = Button(21) 
led = LED(25)

while True: 
	button.wait_for_press()
	led.on() # or, led.blink() or, led.blink(2,2) which means 2 seconds on, 2 seconds off
	button.wait_for_release()
	led.off()"""


from gpiozero import Button, Buzzer, LED
from time import sleep 

red = LED(25)
amber = LED(8)
green = LED(7)
buzzer = Buzzer(15)

while True: 
	button.wait_for_press()
	red.on
	buzzer.beep(.01,1)
	sleep(1)
	amber.on()
	buzzer.beep(.01,1)
	sleep(1)
	green.on()
	buzzer.beep(.01,1)
	buzzer.off()
	sleep(1)
	red.off()
	amber.off()
	green.off()
	

