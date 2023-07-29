import time
import board
import neopixel

#step count between primarys
stepsize = 1
fadecount = (256/stepsize)
redgreen = fadecount
greenblue = 2*fadecount
bluered = 3*fadecount

cyclecount = 3*fadecount

#initialse colours
red = 255
green = 0
blue = 0

#define pixel to rainbow
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
#define pixel brightness
pixel.brightness = 1

#stepcount initialise
count = 0

while (count < (cyclecount+1)):
    colour=(red,green,blue)
    print(count)
    print(colour)
    pixel.fill(colour)
    if (count < redgreen):
        red -= stepsize
        green += stepsize
        if (red < 0):
            red = 0
        if (green > 255):
            green = 255
    elif (count < greenblue):
        green -= stepsize
        blue += stepsize
        if (green < 0):
            green = 0
        if (blue > 255):
            blue = 255
    elif (count < bluered):
        blue -= stepsize
        red += stepsize
        if (blue < 0):
            blue = 0
        if (red > 255):
            red = 255
    count += 1
    if (count == cyclecount):
        count = 0
    time.sleep(0.05)
