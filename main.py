from verilog_parser.systemverilogparser import SystemVerilogParser
from verilog_search.verilogsearch import VerilogSearch

if __name__ == "__main__":
    # Parse the file and get the graph
    parser = SystemVerilogParser('verilog_modules/file.v')
    parser.parse()
    parser.print_modules()
    parser.draw_module_graph()

    # Search in graph
    search = VerilogSearch(parser.get_execution_graph())
    print(f"Longest path is: {search.get_longest_path()}")

