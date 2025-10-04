import RPi.GPIO as GPIO
import time

L1 = 17
L2 = 27
L3 = 22
L4 = 5
L5 = 6
L6 = 26

## Control Line 
CL1 = 4  # Control Line
CC1 = 24 # Space
CC2 = 23 # Enter/Speak
CC3 = 9  # Del/Backspace
CC4 = 10 # NA  


C1 = 21
C2 = 20
C3 = 16
C4 = 7
C5 = 8
C6 = 25
C7 = 24


keypadPressed = -1

input = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(L5, GPIO.OUT)
GPIO.setup(L6, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def keypadCallback(channel):
	global keypadPressed

	if keypadPressed == -1:
		keypadPressed = channel

GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C5, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C6, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C7, GPIO.RISING, callback=keypadCallback)

def setAllLines(state):
	GPIO.output(L1, state)
	GPIO.output(L2, state)
	GPIO.output(L3, state)
	GPIO.output(L4, state)
	GPIO.output(L5, state)
	GPIO.output(L6, state)


def readLine(line, characters):

	global input

	# We have to send a pulse on each line to
	# detect button presses

	GPIO.output(line, GPIO.HIGH)

	if(GPIO.input(C1) == 1):
		input = input + characters[0]

	if(GPIO.input(C2) == 1):
		input = input + characters[1]

	if(GPIO.input(C3) == 1):
		input = input + characters[2]

	if(GPIO.input(C4) == 1):
		input = input + characters[3]

	if(GPIO.input(C5) == 1):
		input = input + characters[4]

	if(GPIO.input(C6) == 1):
		input = input + characters[5]

	if(GPIO.input(C7) == 1):
		input = input + characters[6]

	GPIO.output(line, GPIO.LOW)

try:
	while True:
		if keypadPressed != -1:
			setAllLines(GPIO.HIGH)

			if GPIO.input(keypadPressed) == 0:
				keypadPressed = -1
			else:
				time.sleep(0.1)
		else:
			#if not checkSpecialKeys():
			readLine(L1, ["A","B","C","D","E","F","G"])
			readLine(L2, ["H","I","J","K","L","M","N"])
			readLine(L3, ["O","P","Q","R","S","T","U"])
			readLine(L4, ["V","W","X","Y","Z","0","1"])
			readLine(L5, ["2","3","4","5","6","7","8"])
			readLine(L6, ["9"," ",".",",","?","[ENTER]","<-"])
			##readLine(L7, ["@","#","$","%","^","&","*"])
			print(input, end="")
			time.sleep(0.1)
			#else:
			#	time.sleep(0.1)
except KeyboardInterrupt:
	print("\nApplication stopped!")
	
	
