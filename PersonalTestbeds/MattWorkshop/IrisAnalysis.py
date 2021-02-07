# self.species.where(self.species == "Iris-setosa").dropna();

import pandas as pd;
import numpy as np;

class IrisAnalysis:

    @staticmethod
    def Analyze():
        setosa, versicolor, virginica = IrisAnalysis.__LoadRawData();

    @staticmethod
    def __LoadRawData():
        raw_data = pd.read_csv("DataSets/Iris/Iris.csv");

        setosa_data = raw_data.loc[raw_data.Species == "Iris-setosa"];
        versicolor_data = raw_data.loc[raw_data.Species == "Iris-versicolor_data"];
        virginica_data = raw_data.loc[raw_data.Species == "Iris-virginica"];

        setosa_objects = IrisAnalysis.__GenerateIrisDataSubset(setosa_data);
        versicolor_objects = IrisAnalysis.__GenerateIrisDataSubset(versicolor_data);
        virginica_objects = IrisAnalysis.__GenerateIrisDataSubset(virginica_data);

        # return setosa_data, versicolor_data, virginica_data;
        return setosa_objects, versicolor_objects, virginica_objects;

    @staticmethod
    def __GenerateIrisDataSubset(dataframe):
        subset = [];
        for index, row in dataframe.iterrows():
            subset.append(_IrisData(row["Id"],row["SepalLengthCm"],row["SepalWidthCm"],row["PetalLengthCm"],row["PetalWidthCm"],row["Species"]))

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