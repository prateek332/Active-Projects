# This script needs to run continuosly in seprate process

import re
from pathlib import Path
from Checkers import pathCheck
from InternalWorkingScripts.Components.ComponentsCreator import comp_path


# Making a list of logic gates
def logicGatesList():
    logic_gates_path = Path(str(Path('.').absolute()) + '/DataFiles/DigitalComponents/logic_gates.txt')

    logic_gates = None
    if pathCheck.checkPath(logic_gates_path):
        with open(logic_gates_path) as lg:
            logic_gates = lg.read().split()  # List of logic gates
    else:
        print("'DataFiles/DigitalComponents/logic_gates.txt' does not exists. Please reinstall the program.")
        exit()
    
    return  logic_gates

# Stores the parsed-components data
parsed_components_list = []

'''
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
'''

def _componentsParser(gate_info):
    global parsed_components_list
    parsed_components_list.clear()

    gate_info = gate_info.strip()

    gate_name = re.compile(r'\w{2,4}')
    gate_inputs_quantity = re.compile(r'\d+(\s\d+)?')

    # Getting info
    gate = gate_name.search(gate_info).group()
    _x = gate_inputs_quantity.search(gate_info).group().split()
    # _x[0] = quantity, for NOT gate
    # _x[0] = no_of_inputs, _x[1] = quantity, for all other gates

    if gate != "not":
        parsed_components_list.append([gate,_x[0],_x[1]])
        #NLG.netListCreator(gate,_x[0],_x[1])
    else:
        parsed_components_list.append([gate,1,_x[0]])
        #NLG.netListCreator(gate,quantity=_x[0])

def writeParsedComponents():
    filepath = Path(str(Path('.').absolute()) + '/DataFiles/ParsedComponents/parsed_components.txt')

    if pathCheck.checkPath(filepath):
        pass
    else:
        pathCheck.checkPath(filepath,True)
    
    global parsed_components_list
    with open(filepath, 'w') as wpc:
        wpc.write(str(parsed_components_list))


def parseComponents():
    filepath = comp_path
    with open(filepath) as cp:
        for line in cp:
            if line == '\n' or line[0] == '#':
                continue
            _componentsParser(line)
    writeParsedComponents()
    print(parsed_components_list)


