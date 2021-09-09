import sys
from pygame import midi
from pygame.midi import Input

midi.init()

if (not midi.get_init()):
    exit(1)

i = Input(int(sys.argv[1]))

while True:
    if i.poll():
        midi_events = i.read(10)
        event = midi_events[0][0]
        event.pop()
        print(event)