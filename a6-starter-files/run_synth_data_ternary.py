from ternary_perceptron import TernaryPerceptron  # The classifier and learning are here.
from plot_tp import PlotTernaryPerceptron
import csv  # For reading in data.
from matplotlib import pyplot as plt  # For plotting
import math  # For sqrt.

class PlotMultiTP(PlotTernaryPerceptron):
    """
        Plots the Ternary Perceptron after training it on the iris dataset
        with 4 features and 3 classes.
        """

    def __init__(self, tp, n_epochs, fts):
        super().__init__(tp, n_epochs, fts)  # Calls the constructor of the super class
        self.FEATURES = {0: 'Sepal Length',
                         1: 'Sepal Width',
                         2: 'Petal Length',
                         3: 'Petal Width'}  # Stores the names of the different features for Iris dataset

    def read_data(self):
        """
        Read data from the Iris dataset with 4 features and 2 classes
        for both training and testing.
        ---
        Overrides the method in PlotTernaryPerceptron
        """
        data_as_strings = list(csv.reader(open('synthetic_data.csv'), delimiter=','))
        self.TRAINING_DATA = [[float(f1), float(f2), int(c)]
                              for [f1, f2, c] in data_as_strings]

    def plot(self):
        """
        Plots the dataset as well as the ternary classifier
        """
        points_to_plot = [[I[self.FEATURES_TO_PLOT[0]], I[self.FEATURES_TO_PLOT[1]], I[-1]] for I in self.TRAINING_DATA]
        self.plot_2d_points(points_to_plot)
        self.plot_weight_vectors(self.tp.W)
        plt.xlabel(self.FEATURES[self.FEATURES_TO_PLOT[0]])
        plt.ylabel(self.FEATURES[self.FEATURES_TO_PLOT[1]])
        plt.title("synth data")
        plt.show()


if __name__ == '__main__':
    ternary_perceptron = TernaryPerceptron(alpha=0.5)
    ptp = PlotMultiTP(ternary_perceptron, 50, fts=(0, 2))
    ptp.train()
    ptp.test()
    ptp.plot()