"""run_2_class_2_feature_iris_data.py
YOU SHOULD NOT NEED TO EDIT THIS FILE OR TURN IT IN.
HOWEVER, YOU ARE WELCOME TO EDIT THE FILE TO EXPLORE
POSSIBLE ADJUSTMENTS TO PARAMETERS.

Train a perceptron on the first 10 examples of iris setosa
and the first 10 examples of iris versicolor, considering
only sepal length and petal length as features.

Then test with the remaining 40 examples of each.
Extends the Class PlotBinaryPerceptron

Version 1.1, Prashant Rangarajan and S. Tanimoto, May 11, 2021. Univ. of Washington.
"""

from binary_perceptron import BinaryPerceptron  # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt  # For creating plots.
import remapper as remapper

class PlotRingBP(PlotBinaryPerceptron):
    """
    Plots the Binary Perceptron after training it on the Iris dataset
    ---
    Extends the class PlotBinaryPerceptron
    """

    def __init__(self, bp, plot_all=True, n_epochs=25, IS_REMAPPED=True):
        super().__init__(bp, plot_all, n_epochs)  # Calls the constructor of the super class
        self.IS_REMAPPED = IS_REMAPPED  # Remap the data to be linearly separable

    def read_data(self):
        """
        Read data from the Iris dataset with 2 features and 2 classes
        for both training and testing.
        ---
        Overrides the method in PlotBinaryPerceptron
        """

        data_as_strings_train = list(csv.reader(open('ring-data.csv'), delimiter=','))
        # self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_strings_train]

        # region remap train
        self.TRAINING_DATA = []
        for [f1, f2, c] in data_as_strings_train:
            if self.IS_REMAPPED:
                [f1, f2] = remapper.remap(float(f1), float(f2))
            self.TRAINING_DATA.append([float(f1), float(f2), int(c)])
        # endregion

        data_as_strings_test = list(csv.reader(open('ring-data.csv'), delimiter=','))
        # self.TESTING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_strings_test]

        #region remap test
        self.TESTING_DATA = []
        for [f1, f2, c] in data_as_strings_test:
            if self.IS_REMAPPED:
                [f1, f2] = remapper.remap(float(f1), float(f2))
            self.TESTING_DATA.append([float(f1), float(f2), int(c)])
        #endregion
    def test(self):
        """
        Evaluates the Binary Perceptron on the test set.
        Prints out the number of errors.
        """
        error_count = 0
        N_TESTING = len(self.TESTING_DATA)
        for i in range(N_TESTING):
            x_vec = self.TESTING_DATA[i][:-1]
            y = self.TESTING_DATA[i][-1]
            result = self.bp.classify(x_vec)
            if result != y: error_count += 1
        print(error_count, " errors on the test data, out of ", N_TESTING, "items.")

    def plot(self):
        """
        Plots the dataset as well as the binary classifier
        ---
        Overrides the method in PlotBinaryPreceptron
        """
        plt.title("Iris setosa (blue) vs iris versicolor (red)")
        plt.xlabel("Sepal length")
        plt.ylabel("Petal length")
        plt.legend(loc='best')
        plt.show()


if __name__ == '__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotRingBP(binary_perceptron)
    pbp.train()
    pbp.test()
    pbp.plot()

