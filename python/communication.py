import sys
import json
from pygame import midi
from pygame.midi import Output

midi.init()

if (not midi.get_init()):
    exit(1)

interface, name, input, output, opened = midi.get_device_info(int(sys.argv[1]))

name = str(name).replace("b", "").replace("'", "")
interface = str(interface).replace("b", "").replace("'", "")

type = "Input"
if (output == 1): type = "Output"
if (opened == 0): opened = False
else: opened = True

output = {
    "port": int(sys.argv[1]),
    "interface": interface,
    "name": name,
    "type": type,
    "opened": opened
}

print(json.dumps(output))

midi.quit()