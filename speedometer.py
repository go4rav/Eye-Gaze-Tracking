import main2
import os
def speed():
	while True:
		os.system("cls")
		print("\n\n\n\t\t Current speed: ", main2.speed)
		speed = int(input("\n\t\tEnter new speed: \t "))
		if speed==-1:
			break
		else:
			main2.speed=speed
