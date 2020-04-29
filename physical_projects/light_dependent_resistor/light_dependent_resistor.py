# a capacitor is an electrical component that stores charge
# when current is fed into a capacitor, it will begin to store charge

# by putting a resistor in series with the capacitor, you can slow the speed at which it charges

# for a Raspberry Pi, any input that is approximately below 1.8V is considered 'off' and any above 1.8V is considered 'on' ; for output, 0V is off and 3.3V is on

# if you time how long it takes the capacitor's voltage to get over 1.8V you can work out the resistence of the component in series with it 

# an LDR (photocell) is a special type of resistor; when light hits it, resistence is low, but when it's dark, resistance is high 

# by placing a capacitor in series with an LDR, the capacitor will charge at different speeds depending on whether it's light or dark

from gpiozero import LightSensor, Buzzer

ldr = LightSensor(4) 
while True: 
	print(ldr.value) 