# GPIO pints are digital, so you can only set outputs to high or low, or read inputs as high or low
# using an ADC chip (Analogue-to-Digital converter) you can read the value of analogue input devices like potentiometers

# analogue values are communicated to the Pi using the SPI protocol

# open a terminal window and install spidev package 

### sudo apt-get install python3-spidev python-spidev

### open Raspberry Pi Configuration from main menu and enable "SPI" in the Interfaces tab

from gpiozero import MCP3008

pot = MCP3008(0)

# print(pot.value) # try to read potentiometer's value

### next, add an LED to your breadboard and wire it to the Pi, connecting it to GPIO pin 21

from gpiozero import PWMLED # lets you control the brightness of an LED using PWM (pulse-width modulation) 

led = PWMLED(21) 

led.source = pot.values # turn the dial to change the LED brightness! 
