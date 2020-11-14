import re
from pathlib import Path
from ..NetList import NetListGenerator as NLG

# All possible logic_gates
logic_gates = ['and','or','not','nand','nor','xor','xnor']
netlist_data = []

def infoChecker(gate, inputs = '1', quantity = '1'):
    if gate not in logic_gates:
        print("Gate name: ", gate, " does not exits.")
        exit()

    if gate == 'not':
        if inputs != '1':
            print("NOT gate inputs quantity are invalid.")
            exit()
        if quantity < '1':
            print("NOT gate quantity are invalid.")

    else:
        if inputs < '1':
            print("Wrong number of inputs for Gate:",gate)
            exit()
        if quantity < '1':
            print("Invalid quantity for Gate:",gate)
            exit()
    
    # Just to check if program works correctly.
    # Remove this in final product.
    print("Info is correct")

def _componentsParser(gate_info):
    gate_info = gate_info.strip()

    gate_name = re.compile(r'\w{2,4}')
    gate_inputs_quantity = re.compile(r'\d+(\s\d+)?')

    # Getting info
    gate = gate_name.search(gate_info).group()
    _x = gate_inputs_quantity.search(gate_info).group().split()
    # _x[0] = quantity, for NOT gate
    # _x[0] = no_of_inputs, _x[1] = quantity, for all other gates

    if gate != "not":
        netlist_data.append([gate,_x[0],_x[1]])
        #NLG.netListCreator(gate,_x[0],_x[1])
    else:
        netlist_data.append([gate,1,_x[0]])
        #NLG.netListCreator(gate,quantity=_x[0])


def parseComponents(file_path):
    with open(file_path) as cp:
        for line in cp:
            if line == '\n' or line[0] == '#':
                continue
            _componentsParser(line)
    NLG.netListCreator(netlist_data)
