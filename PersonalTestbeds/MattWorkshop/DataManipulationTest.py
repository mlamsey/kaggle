import pandas as pd;

class DataManipulationTest:

  @staticmethod
  def Read(file_path,delimiter):
    data_frame = pd.read_csv(file_path,delimiter=delimiter);

    print("Data Frame shape:");
    print(data_frame.shape);

    for row in data_frame.values:
      print(row);