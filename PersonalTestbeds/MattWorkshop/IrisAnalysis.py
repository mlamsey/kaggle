import pandas as pd;
import matplotlib.pyplot as plt;
import numpy as np;

class IrisAnalysis:

    @staticmethod
    def Analyze():
        iris_data = IrisAnalysis.__LoadRawData();
        IrisAnalysis.__PlotAllMetrics(iris_data);

    @staticmethod
    def __LoadRawData():
        raw_data = pd.read_csv("DataSets/Iris/Iris.csv");

        # Labels manually extracted from first row of csv
        index = raw_data.values[:,0];
        sepal_length = raw_data.values[:,1];
        sepal_width = raw_data.values[:,2];
        petal_length = raw_data.values[:,3];
        petal_width = raw_data.values[:,4];
        species = raw_data.values[:,5];

        return _IrisData(index, sepal_length, sepal_width, petal_length, petal_width, species);

    @staticmethod
    def __PlotAllMetrics(data):
        plt.scatter(data.index,data.sepal_length);
        plt.scatter(data.index,data.sepal_width);
        plt.scatter(data.index,data.petal_length);
        plt.scatter(data.index,data.petal_width);

        plt.gca().grid(which='major',color='silver');
        plt.gca().legend(["Sepal Length", "Sepal Width", "Petal Length","Petal Width"]);
        plt.title("All Iris Metrics");
        plt.xlabel("Index");
        plt.ylabel("Metric Value (cm)");

        plt.show();

# Private Classes
class _IrisData:
    def __init__(self, index, sepal_length, sepal_width, petal_length, petal_width, species):
        # via first line of csv
        self.index = index;
        self.sepal_length = sepal_length;
        self.sepal_width = sepal_width;
        self.petal_length = petal_length;
        self.petal_width = petal_width;
        self.species = species;