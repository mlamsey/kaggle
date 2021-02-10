import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

class IrisAnalysis:
    n_round = 3;

    @staticmethod
    def Analyze():
        setosa, versicolor, virginica = IrisAnalysis.__LoadRawData();
        IrisAnalysis.__CalculateSepalLengthMeans(setosa, versicolor, virginica);
        IrisAnalysis.__SepalLengthHistograms(setosa, versicolor, virginica);

    @staticmethod
    def __LoadRawData():
        raw_data = pd.read_csv("DataSets/Iris/Iris.csv");

        setosa_data = raw_data.loc[raw_data.Species == "Iris-setosa"];
        versicolor_data = raw_data.loc[raw_data.Species == "Iris-versicolor"];
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
            subset.append(_IrisData(row["Id"],row["SepalLengthCm"],row["SepalWidthCm"],row["PetalLengthCm"],row["PetalWidthCm"],row["Species"]));

        return subset;

    @staticmethod
    def __CalculateSepalLengthMeans(setosa, versicolor, virginica):
        setosa_sepal_lengths = [iris.sepal_length for iris in setosa];
        versicolor_sepal_lengths = [iris.sepal_length for iris in versicolor];
        virginica_sepal_lengths = [iris.sepal_length for iris in virginica];

        setosa_sepal_length_mean = np.mean(setosa_sepal_lengths)
        setosa_sepal_length_std = np.std(setosa_sepal_lengths)
        print("Setosa Mean Sepal Length: " + str(round(setosa_sepal_length_mean,IrisAnalysis.n_round)) + " | Setosa Stddev Sepal Length: " + str(round(setosa_sepal_length_std,IrisAnalysis.n_round)))

        versicolor_sepal_length_mean = np.mean(versicolor_sepal_lengths)
        versicolor_sepal_length_std = np.std(versicolor_sepal_lengths)
        print("Versicolor Mean Sepal Length: " + str(round(versicolor_sepal_length_mean,IrisAnalysis.n_round)) + " | Versicolor Stddev Sepal Length: " + str(round(versicolor_sepal_length_std,IrisAnalysis.n_round)))

        virginica_sepal_length_mean = np.mean(virginica_sepal_lengths)
        virginica_sepal_length_std = np.std(virginica_sepal_lengths)
        print("Virginica Mean Sepal Length: " + str(round(virginica_sepal_length_mean,IrisAnalysis.n_round)) + " | Virginica Stddev Sepal Length: " + str(round(virginica_sepal_length_std,IrisAnalysis.n_round)))
        
        return setosa_sepal_length_mean, versicolor_sepal_length_mean, virginica_sepal_length_mean;

    @staticmethod
    def __SepalLengthHistograms(setosa, versicolor, virginica):
        setosa_sepal_lengths = [iris.sepal_length for iris in setosa];
        versicolor_sepal_lengths = [iris.sepal_length for iris in versicolor];
        virginica_sepal_lengths = [iris.sepal_length for iris in virginica];

        plt.hist(setosa_sepal_lengths,10);
        plt.hist(versicolor_sepal_lengths,10);
        plt.hist(virginica_sepal_lengths,10);

        plt.legend(["Setosa", "Versicolor", "Virginica"])

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