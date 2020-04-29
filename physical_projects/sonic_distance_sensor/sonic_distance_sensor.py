# the sensor sends pulses of ultrasound and detects the echo sent back when sound bounces off nearby object
# it uses speed of sound (353 meters per second) to calculate distance from the object

from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)
while True: 
	print(ultrasonic.distance) 

# TO GET THE SENSOR TO ACT WHEN AN OBJECT IS IN OR OUT OF A CERTAIN RANGE #

while True: 
	ultrasonic.wait_for_in_range()
	print("In range") 
	ultrasonic.wait_for_out_of_range()
	print("Out of range") 

# the default range threshold is .3m, but that can be configured when the sensor is initiated

#ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=.5)

# /// # /// # /// # /// # /// # /// 

# you can also use a UDF to make action when the threshold is breached

"""def hello(): 
	print("Hello")

def bye(): 
	print("Bye")

ultrasnoic.when_in_range = hello 
ultrasonic.when_out_of_range = bye"""