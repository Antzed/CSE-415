from binary_perceptron import BinaryPerceptron  # The classifier and learning are here.
from plot_bp import PlotBinaryPerceptron
import csv  # For reading in data.
from matplotlib import pyplot as plt  # For plotting
import math  # For sqrt.

class PlotMultiBPOneVsOne(PlotBinaryPerceptron):
    def __init__(self, bp, plot_all=True, n_epochs=50):
        super().__init__(bp, plot_all, n_epochs)  # Calls the constructor of the super class
        self.CLASSES = (0, 1)

    def read_data(self):
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        processed_data = []
        for i in data_as_strings:
            if int(i[-1]) in self.CLASSES:
                processed_data.append(i)

        self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in  processed_data]
        for i in self.TRAINING_DATA:
            if i[-1] == self.CLASSES[0]:
                i[-1] = 1
            else:
                i[-1] = -1


    def plot(self):
        plt.title("one v one with class" + str(self.CLASSES))
        plt.legend(loc='best')
        plt.show()

if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotMultiBPOneVsOne(binary_perceptron)
    pbp.train()
    pbp.plot()