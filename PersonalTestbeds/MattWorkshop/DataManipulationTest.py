import pandas as pd;
import matplotlib.pyplot as plt;

class DataManipulationTest:

  @staticmethod
  def Read(file_path,delimiter):
    data_frame = pd.read_csv(file_path,delimiter=delimiter);

    print("Data Frame shape:");
    print(data_frame.shape);

    return data_frame;
  
  @staticmethod
  def Plot(x,y):
    print('DataManipulationTest::Plot');
    fig, ax = plt.subplots();
    ax.plot(x,y);
    ax.set_title("Plot Title!");
    ax.set_xlabel('Index');
    ax.set_ylabel('Parameter');
    ax.grid(which='major',color='silver');

    plt.show();

  @staticmethod
  def Scatter(x,y):
    print('DataManipulationTest::Scatter');
    fig, ax = plt.subplots();
    ax.scatter(x,y);
    ax.set_title("Plot Title!");
    ax.set_xlabel('X Value');
    ax.set_ylabel('Y Value');
    ax.grid(which='major',color='silver');

    plt.show();