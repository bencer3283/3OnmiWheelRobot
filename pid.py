from gpiozero import Motor, DigitalInputDevice
from time import sleep

motorA = Motor(7, 8)
motorB = Motor(9, 10)
motorC = Motor(14, 15)

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

encoderA = Encoder(17)
encoderB = Encoder(27)
encoderC = Encoder(22)

motorA.forward(0.2)
motorB.forward(0.2)
motorC.forward(0.2)

if __name__ == '__main__':
    while True:
        print("A: {}, B: {}, C: {}".format(encoderA.value, encoderB.value, encoderC.value))
        sleep(1)