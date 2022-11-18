import os

x = input()

os.system("echo "+ x +" > /sys/class/backlight/amdgpu_bl1/brightness")

os.system("exit")