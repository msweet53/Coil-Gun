import board
import time
from digitalio import DigitalInOut, Direction, Pull
import analogio

interrupter = DigitalInOut(board.D6)
relay = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP
relay.direction = Direction.OUTPUT
x = 0

a = analogio.AnalogIn(board.A0)

while True:
    if interrupter.value:
        print(interrupter.value)
        relay.value = True
        while interrupter.value:
            pass
        else:
            relay.value = False