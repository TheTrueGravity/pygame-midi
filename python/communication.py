import sys
import json
from pygame import midi
from pygame.midi import Output

midi.init()

if (not midi.get_init()):
    exit(1)
    
def get_device_info(id: int):
    if (midi.get_device_info(id) == None):
        return "invalid_device_id"

    interface, name, input, output, opened = midi.get_device_info(id)

    name = str(name).replace("b", "").replace("'", "")
    interface = str(interface).replace("b", "").replace("'", "")

    type = "Input"
    if (output == 1): type = "Output"
    if (opened == 0): opened = False
    else: opened = True

    output = {
        "port": id,
        "interface": interface,
        "name": name,
        "type": type,
        "opened": opened
    }

    return output

if (sys.argv[1] == "get_device_info"):
    device_id = int(sys.argv[2])
    device_info = get_device_info(device_id)
    print(json.dumps(device_info))

elif (sys.argv[1] == "get_all_devices"):
    port_count = midi.get_count()
    output = []
    for i in range(port_count):
        output.append(get_device_info(i))
    print(json.dumps(output))

elif (sys.argv[1] == "get_device_count"):
    print(midi.get_count())

midi.quit()