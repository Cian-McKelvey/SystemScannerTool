import matplotlib.pyplot as plt


class Plotter:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, list_obj, xaxis_name, yaxis_name, title):
        self.list_obj = list_obj
        self.xaxis_name = xaxis_name
        self.yaxis_name = yaxis_name
        self.title = title

    def plot_graph(self):
        plt.plot(self.list_obj)
        plt.xlabel(self.xaxis_name)
        plt.ylabel(self.yaxis_name)
        plt.title(self.title)
        plt.show()
