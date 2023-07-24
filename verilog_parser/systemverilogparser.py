import networkx as nx
from matplotlib import pyplot as plt


def _get_module_name(line):
    """
    Gets the module name from current line
    :param line: String contains characters for current line
    :return: The name of the module extracted from the line
    """
    module_name = line.split()[1]
    if '(' in module_name:
        module_name = module_name.split('(')[0]
    return module_name


class SystemVerilogParser:
    def __init__(self, file_path):
        """
        Constructor for SystemVerilogParser class
        :param file_path: Path of the file with verilog code
        """
        self.__file_path = file_path
        self.__modules = {}
        self.__module_graph = nx.DiGraph()

    def parse(self):
        """
        Analyze content of file line by line and gets the modules and generate the graph of execution
        :return:
        """
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith('module'):
                    module_name = _get_module_name(line)
                    self.__modules[module_name] = []
                    self.__module_graph.add_node(module_name)

                    # Search for module instances within this module
                    i += 1
                    while not lines[i].strip().startswith('endmodule'):
                        words = lines[i].strip().split()
                        if len(words) > 0 and words[0] in self.__modules:
                            instance_module = words[0]
                            while instance_module in self.__modules[module_name]:
                                instance_module += "."
                            self.__modules[module_name].append(instance_module)
                            self.__module_graph.add_edge(module_name, instance_module)
                        i += 1
                i += 1

    def print_modules(self):
        """
        Print every module and the dependencies that are used
        :return:
        """
        for module, instances in self.__modules.items():
            print('Module:', module)
            for instance in instances:
                print('   Instance:', instance)

    def draw_module_graph(self):
        """
        Draws the representation of flow as a directed graph
        :return:
        """
        nx.draw(self.__module_graph, with_labels=True)
        plt.show()

    def get_execution_graph(self):
        """
        Getter for graph representation
        :return: Graph as a nx object
        """
        return self.__module_graph
