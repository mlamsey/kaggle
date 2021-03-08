import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;

# Scikit stuff
from sklearn import metrics;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.linear_model import LogisticRegression;
from sklearn.model_selection import train_test_split;

class IrisAnalysis:
    n_round = 3;

    @staticmethod
    def Analyze():
        raw_data = IrisAnalysis.__LoadRawData();
        print(raw_data['Species'].value_counts());
        print("\nRaw Data Head:\n");
        print(raw_data.head());

        # drop Id column
#        plottable_data = raw_data.drop('Id',axis = 1);
#        print("\nClean Data Head:\n");
#        print(plottable_data.head());

#        sns.pairplot(plottable_data, hue = 'Species', markers = '+');
#        plt.show();
        
        IrisAnalysis.__Learn(raw_data);
        
        # setosa, versicolor, virginica = IrisAnalysis.__LoadSeparatedData();
        # IrisAnalysis.__CalculateSepalLengthMeans(setosa, versicolor, virginica);
        # IrisAnalysis.__SepalLengthHistograms(setosa, versicolor, virginica);

    @staticmethod
    def __LoadSeparatedData():
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
    def __LoadRawData():
        return pd.read_csv("DataSets/Iris/Iris.csv");

    @staticmethod
    def __Learn(raw_data):
        print("Learning!");
        y = raw_data['Species'];
        x = raw_data.drop(['Id', 'Species'], axis = 1);

#        print(x.shape);
#        print(y.shape);

#        n_neighbors = 10;
#        score = IrisAnalysis.__KNeighbors(x,y,n_neighbors);
#        print("For " + str(n_neighbors) + " neighbors, the accuracy score is " + str(score));

        scores = [];
        test_range = np.linspace(0.01,0.75,num=75);
        neighbors_range = np.linspace(1,25,num=25);
        for t in test_range:
            scores_row = []
            for n in neighbors_range:
                scores_row.append(IrisAnalysis.__KNeighbors(x,y,int(n),t));
            scores.append(scores_row);
        
        scores = np.transpose(np.array(scores));
        X,Y = np.meshgrid(test_range,neighbors_range);

        fig, ax = plt.subplots(subplot_kw = {"projection":"3d"});

        ax.plot_surface(X,Y,scores);
        ax.set_xlabel('Test Range (Percent)');
        ax.set_ylabel('Number of Neighbors');
        ax.set_zlabel('Accuracy (Percent)');
        ax.set_title('K-Nearest Neighbors: Iris Dataset');
        plt.show();

    @staticmethod
    def __KNeighbors(x,y,n_neighbors,test_size):
        x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = test_size, random_state = None);

        knn = KNeighborsClassifier(n_neighbors = n_neighbors);
        knn.fit(x_train,y_train);
        y_predicted = knn.predict(x_test);
        
        return metrics.accuracy_score(y_test,y_predicted);

    @staticmethod
    def __LogisticRegression(x,y):
        # learn
        1;

    @staticmethod
    def __ModelSelection(x,y):
        # select model
        1;

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
