from binary_perceptron import BinaryPerceptron  # The classifier and learning are here.
from plot_bp import PlotBinaryPerceptron
import csv  # For reading in data.
from matplotlib import pyplot as plt  # For plotting
import math  # For sqrt.

class PlotMultiBPOneVsAll(PlotBinaryPerceptron):
    def __init__(self, bp, plot_all=False, n_epochs=50):
        super().__init__(bp, plot_all, n_epochs)  # Calls the constructor of the super class
        self.positive = 2

    def read_data(self):
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_strings]
        for i in self.TRAINING_DATA:
            if i[-1] == self.positive:
                i[-1] = 1
            else:
                i[-1] = -1

    def plot(self):
        plt.title("one v all with positive value of "+ str(self.positive))
        plt.legend(loc='best')
        plt.show()

if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotMultiBPOneVsAll(binary_perceptron)
    pbp.train()
    pbp.plot()