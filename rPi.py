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

motorA = Motor(7, 8)
motorB = Motor(9, 10)
motorC = Motor(14, 15)

def stop():
    motorC.stop()
    motorA.stop()
    motorB.stop()

def forward():
    motorA.backward(0.5)
    motorB.forward(0.5)
    while True:
        if blue.read(1) == b's':
            break

def backward():
    motorA.forward(0.5)
    motorB.backward(0.5)
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
    motorA.forward(0.5)
    motorB.forward(0.5)
    motorC.forward(0.5)
    while True:
        if blue.read(1) == b's':
            break
    

def counterclockwise():
    motorA.backward(0.5)
    motorB.backward(0.5)
    motorC.backward(0.5)
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
        

