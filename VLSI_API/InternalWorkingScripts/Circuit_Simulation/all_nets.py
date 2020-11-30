from InternalWorkingScripts import filePath
import json

netlist_path = filePath().netlist_txt_path()
all_nets_path = filePath().all_nets()



def parse_all_nets():
    all_nets = {}
    with open(netlist_path) as fp:
        for line in fp:
            nets = line.split()
            # removing the component name
            nets = nets[1:]
            for n in nets:
                all_nets[n] = "ND" # Using `ND` for not defined
    with open(all_nets_path, 'w') as fp:
        json.dump(all_nets, fp, indent=4)


            
