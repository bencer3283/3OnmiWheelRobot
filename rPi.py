from gpiozero import Motor, Robot, DigitalInputDevice
from time import sleep
import serial

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
    sleep(0.5)
    stop()

def backward():
    motorA.forward(0.5)
    motorB.backward(0.5)
    sleep(0.5)
    stop()

def left():
    motorA.forward(0.353)
    motorB.forward(0.353)
    motorC.backward(0.863)
    sleep(0.5)
    stop()

def right():
    motorA.backward(0.353)
    motorB.backward(0.353)
    motorC.forward(0.863)
    sleep(0.5)
    stop()

if __name__ == '__main__': 
    while run:
        stop()
        cmdFromHost = input()
        print(cmdFromHost)
        if cmdFromHost == 'quit':
            run = False
        elif cmdFromHost == 'f':
            forward()
        elif cmdFromHost == 'b':
            backward()
        elif cmdFromHost == 'l':
            left()
        elif cmdFromHost == 'r':
            right()
        

