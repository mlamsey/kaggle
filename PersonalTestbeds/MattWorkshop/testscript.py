import numpy as np;

# Add Folder containing classes to system path
import sys;
sys.path.insert(1, 'PersonalTestbeds/MattWorkshop');

# # Import class definition
# from TestClass import TestClass;

# t = TestClass(2);
# t.TestNumber();

# # Static method + recursion test
# n_terms = 7;
# fibonacci_sum = TestClass.RecursiveFibonacci(n_terms);
# print("The sum of the first " + str(n_terms) + " numbers in the Fibonacci Sequence is "+ str(fibonacci_sum));

# # Plotting test
# from LibraryDemo import LibraryDemo;
# LibraryDemo.PlotTest();

# Data Manipulation Test
from DataManipulationTest import DataManipulationTest;
file_path = "DataSets/Iris/Iris.csv";
test_data = DataManipulationTest.Read(file_path,",");

y_values = test_data.values[:,2];
x_values = np.linspace(0,y_values.size,y_values.size);

DataManipulationTest.Plot(x_values,y_values);