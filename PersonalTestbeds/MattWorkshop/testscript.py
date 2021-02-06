# Add Folder containing class to system path
import sys;
sys.path.insert(1, 'MattWorkshop');

# Import class definition
from TestClass import TestClass;

t = TestClass(2);
t.TestNumber();

# Static method + recursion test
n_terms = 7;
fibonacci_sum = TestClass.RecursiveFibonacci(n_terms);
print("The sum of the first " + str(n_terms) + " numbers in the Fibonacci Sequence is "+ str(fibonacci_sum));

# Plotting test
from LibraryDemo import LibraryDemo;
LibraryDemo.PlotTest();