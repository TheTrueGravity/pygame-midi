import sys
import json
from pygame import midi
from pygame.midi import Output

midi.init()

if (not midi.get_init()):
    exit(1)

o = Output(int(sys.argv[1]))

if (len(sys.argv) > 2):
    data = json.loads(sys.argv[2])

    o.write_short(data[0], data[1], data[2])
else:
    while True:
        print("Ready!")
        
        data = json.loads(input())

        o.write_short(data[0], data[1], data[2])
