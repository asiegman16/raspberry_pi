# a PIR sensor detects changes in the amount of infared radiation it receives
# when there's a significant change in IR it detects, a pulse is triggered
# thus, a PIR sensor can detect when a human (or any animal_ moves in front of it 

# DETECTING MOTION

from gpiozero import MotionSensor

pir = MotionSensor(4)

while True: 
	pir.wait_for_motion()
	print("You moved")
	pir.wait_for_no_motion()

	