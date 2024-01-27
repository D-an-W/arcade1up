from gpiozero import Button
import os
Button(3).wait_for_release()
os.system("sudo shutdown now -h")
