from pathlib import Path
import json

gate_codes_file_path = Path(str(Path.cwd()) + '/VLSI_Python/InternalWorkingScripts/Gate_Codes.json')

Gate_Codes = None

from pathlib import Path

def gateAndIndex(gate,Gate_Codes):
    gate_code = Gate_Codes[gate][0]
    gate_index = Gate_Codes[gate][1]
    Gate_Codes[gate][1] += 1
    return gate_code, str(gate_index)

def netListHelper(gate, inputs = None, quantity = None):
    result = ""
    tmp = inputs
    while quantity != 0:
        g_code, g_index = gateAndIndex(gate,Gate_Codes)
        netlist = g_code + g_index
        pins = netlist
        k = 1
        while tmp != 0:
            pins += " " + g_code + g_index + str(k)
            tmp -= 1
            k += 1
        pins += " " + g_code + g_index + 'o'
        result = result + pins + '\n'
        tmp = inputs
        quantity -= 1
    return result

def netListCreator(netlist_data):
    Gate_Codes = {}
    with open(gate_codes_file_path) as gc:
        print("Done")
        Gate_Codes = json.load(gc)
    
    net_list_file_path = Path(str(Path.cwd()) + '/netlist.txt')
    with open(net_list_file_path,'a') as nl:
        for data in netlist_data:
            netlist = netListHelper(data[0], int(data[1]), int(data[2]))
            nl.write(netlist)
            nl.write('\n')
    
    with open(gate_codes_file_path,'w') as gc:
        json.dump(Gate_Codes,gc)
