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

# # Data Manipulation Test
# from DataManipulationTest import DataManipulationTest;
# file_path = "DataSets/Iris/Iris.csv";
# test_data = DataManipulationTest.Read(file_path,",");

# # Line Plot
# # x_values = test_data.values[:,0];
# # y_values = test_data.values[:,1];

# # DataManipulationTest.Plot(x_values,y_values);

# # Scatter Plot
# x_values = test_data.values[:,1];
# y_values = test_data.values[:,2];

# DataManipulationTest.Scatter(x_values,y_values);

# Iris Analysis
from IrisAnalysis import IrisAnalysis;
IrisAnalysis.Analyze();