from gpiozero import Motor, DigitalInputDevice
from time import sleep

motorA = Motor(24, 23)
motorB = Motor(27, 22)
motorC = Motor(17, 18)

class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        encoder = DigitalInputDevice(pin)
        encoder.when_activated = self._increment
        encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0
    def _increment(self):
        self._value += 1
    @property
    def value(self):
        return self._value

encoderA = DigitalInputDevice(16) #Encoder(16)
encoderB = DigitalInputDevice(20) #Encoder(20)
encoderC = DigitalInputDevice(21) #Encoder(21)

motorA.forward(0.2)
motorB.forward(0.2)
motorC.forward(0.2)

readB = True
valueB = 0

readA = True
valueA = 0

readC = True
valueC = 0

if __name__ == '__main__':
    while True:
        #print(DigitalInputDevice(20).value)
        #print("A: {}, B: {}, C: {}".format(encoderA.value, encoderB.value, encoderC.value))
        if encoderB.value != readB:
            valueB += 1
            readB = not readB
        if encoderC.value != readC:
            valueC += 1
            readC = not readC
        if encoderA.value != readA:
            valueA += 1
            readA = not readA
        print("A: {}, B: {}, C: {}".format(valueA, valueB, valueC))
        sleep(0.01)
