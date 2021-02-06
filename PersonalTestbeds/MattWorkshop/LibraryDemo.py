import numpy as np
import matplotlib.pyplot as plt

class LibraryDemo:

  @staticmethod
  def PlotTest():
    x, y = LibraryDemo.__GenerateTestSignal();
    LibraryDemo.__Plot(x,y);

  # Private methods
  @staticmethod
  def __Plot(x,y):
    fig, ax = plt.subplots();
    ax.plot(x,y);
    plt.show();

  @staticmethod
  def __GenerateTestSignal():
    x = np.linspace(0,10,1000);
    y = np.sin(x);

    return x,y;