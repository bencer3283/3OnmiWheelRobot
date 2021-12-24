from gpiozero import Motor, DigitalInputDevice
from time import sleep
import serial
from serial.serialposix import Serial

blue = serial.Serial('/dev/rfcomm0')
try:
    arduino = serial.Serial('/dev/ttyACM0', 115200)
except:
    arduino = serial.Serial('/dev/ttyACM1', 115200)

run = True

motorA = Motor(24, 23)
motorB = Motor(27, 22)
motorC = Motor(17, 18)

def stop():
    c = motorC.value
    b = motorB.value
    a = motorA.value
    if c > 0 :
        motorC.forward(c*2/3)
    if c < 0 :
        motorC.backward(-c*2/3)
    if b > 0 :
        motorB.forward(b*2/3)
    if b < 0 :
        motorB.backward(-b*2/3)
    if a > 0 :
        motorA.forward(a*2/3)
    if a < 0 :
        motorA.backward(-a*2/3)
    sleep(0.2)
    if c > 0 :
        motorC.forward(c/3)
    if c < 0 :
        motorC.backward(-c/3)
    if b > 0 :
        motorB.forward(b/3)
    if b < 0 :
        motorB.backward(-b/3)
    if a > 0 :
        motorA.forward(a/3)
    if a < 0 :
        motorA.backward(-a/3)
    sleep(0.2)
    motorC.stop()
    motorA.stop()
    motorB.stop()

def forward():
    motorA.backward(0.1)
    motorB.forward(0.1)
    sleep(0.2)
    motorA.backward(0.55)
    motorB.forward(0.55)
    sleep(0.2)
    motorA.backward(0.85)
    motorB.forward(0.85)
    while True:
        if blue.read(1) == b's':
            break

def backward():
    motorA.forward(0.15)
    motorB.backward(0.15)
    sleep(0.2)
    motorA.forward(0.55)
    motorB.backward(0.55)
    sleep(0.2)
    motorA.forward(0.85)
    motorB.backward(0.85)
    while True:
        if blue.read(1) == b's':
            break

def left():
    motorA.forward(0.353)
    motorB.forward(0.353)
    motorC.backward(0.863)
    while True:
        if blue.read(1) == b's':
            break

def right():
    motorA.backward(0.353)
    motorB.backward(0.353)
    motorC.forward(0.863)
    while True:
        if blue.read(1) == b's':
            break

def clockwise():
    motorA.forward(0.25)
    motorB.forward(0.25)
    motorC.forward(0.25)
    while True:
        if blue.read(1) == b's':
            break
    

def counterclockwise():
    motorA.backward(0.25)
    motorB.backward(0.25)
    motorC.backward(0.25)
    while True:
        if blue.read(1) == b's':
            break
    

if __name__ == '__main__': 
    while run:
        stop()
        cmdFromHost =  blue.read(1) #input()
        print(cmdFromHost)
        if cmdFromHost == b's':
            stop()
        elif cmdFromHost == b'f':
            forward()
            #print('forward')
        elif cmdFromHost == b'b':
            backward()
            #print('backward')
        elif cmdFromHost == b'l':
            left()
            #print('left')
        elif cmdFromHost == b'r':
            right()
            #print('right')
        elif cmdFromHost == b'u':
            arduino.write(b'u')
        elif cmdFromHost == b'd':
            arduino.write(b'd')
        elif cmdFromHost == b'c':
            counterclockwise()
        elif cmdFromHost == b'w':
            clockwise()
        

