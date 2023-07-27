# Verilog-Parser

A simple parser for System Verilog that creates the flow of execution based on modules call.

## Solution

The solution was implemented using Python programming language with help of two modules:
- **networkx** - a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- **matplotlib** - a comprehensive library for creating static, animated, and interactive visualizations in Python.

We created two classes to solve the problem. 
<br><br>**SystemVerilogParser**, as the name suggests, has the role to parse the content of a _.v_ file and to generate a _networkx_ object.
<br><br>**VerilogSearch** applies a BFS (Breadth First Search) algorithm to calculate the height of the tree of execution.

## Results

The following image ilustrates the result obtained on a simple System Verilog code:

![Network of code](https://imgur.com/He1rNYH.png)



