import gpiozero as GPIO
from time import sleep
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

volumeState = 0

while True:
        buttonState1 = GPIO.input(12)
        buttonState2 = GPIO.input(16)

        if buttonState1 == False and buttonState2 == False and volumeState != 88:
                print("Switch was set to Vol HIGH")
                print(volumeState)
                call(["amixer", "set", "HDMI", "unmute"])
                call(["amixer", "set", "HDMI", "88%"])
                volumeState = 88
                sleep(1)

        if buttonState1 == True and buttonState2 == True and volumeState != 0:
                print("Switch was set to MUTE")
                print(volumeState)
                call(["amixer", "set", "HDMI", "mute"])
                volumeState = 0
                sleep(1)

        if buttonState1 == True and buttonState2 == False and volumeState != 68:
                print("Switch was set to Vol LOW")
                print(volumeState)
                call(["amixer", "set", "HDMI", "unmute"])
                call(["amixer", "set", "HDMI", "68%"])
                volumeState = 68
                sleep(1)
