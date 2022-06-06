import matplotlib.pyplot as plt
import numpy as np

# Food name -> array
# Weights -> array
# Solution array -> array


class Report:
    def __init__(self, food_name, weights, sol_arr, price) -> None:
        self.w = weights
        self.dim = len(sol_arr)
        self.vector_constant = sol_arr[0]
        self.food_n = food_name
        self.figure = plt.figure(dpi=150)
        self.coords = [0, self.vector_constant]
        self.price = price

    def visualize_vector(self):
        # Dimensões maiores que 3 é impossível de mostrar
        if self.dim > 3:
            print('Dimensão inválida. Válida para 1 <=dim N <= 3.')
        elif self.dim == 3:
            self.plot_3d()
        elif self.dim == 2:
            self.plot_2d()
        elif self.dim == 1:
            self.plot_1d_in_2d()

    def plot_3d(self):
        ax = self.figure.add_subplot(111, projection='3d')
        ax.view_init(elev=0., azim=0)
        plt.title('Coordinates')
        ax.set_xlabel(f'{self.food_n[0].title()}')
        ax.set_ylabel(f'{self.food_n[1].title()}')
        ax.set_zlabel(f'{self.food_n[2].title()}')
        plt.grid(color='gray', ls='-')

        ax.plot3D(self.coords, self.coords, self.coords, color='g')
        ax.scatter(self.vector_constant,
                   self.vector_constant, self.vector_constant, color='b')
        ax.text(self.vector_constant, self.vector_constant, self.vector_constant,
                f'({self.vector_constant:.3f}, {self.vector_constant:.3f},{ self.vector_constant:.3f})', size=12, zorder=1, color='blue')
        plt.show()

    def plot_2d(self):
        plt.grid(color='gray', ls='-')
        plt.title('Kg Coordinates')
        plt.xlabel(f'{self.food_n[0].title()}')
        plt.ylabel(f'{self.food_n[1].title()}')
        plt.plot(self.coords, self.coords, color='r')
        plt.scatter(self.vector_constant, self.vector_constant, color='b')
        plt.annotate(f'({self.vector_constant:.2f},{self.vector_constant:.2f})',
                     (self.vector_constant, self.vector_constant),
                     textcoords="offset points",
                     xytext=(0, 3),
                     ha='center',
                     color='black',
                     fontsize=12,
                     weight="bold")
        plt.show()

    def plot_1d_in_2d(self):
        plt.grid(color='gray', ls='-')
        plt.title('Kg Coordinates')
        plt.xlabel(f'Alimento {self.food_n[0]}')
        plt.plot(self.coords, [0, 0], color='r')
        plt.scatter(self.vector_constant, 0, color='b')
        plt.annotate(f'({self.vector_constant:.2f})',
                     (self.vector_constant, 0),
                     textcoords="offset points",
                     xytext=(0, 3),
                     ha='center',
                     color='black',
                     fontsize=12,
                     weight="bold")
        plt.show()

    def visualize_bar_pollution(self):
        plt.grid(color='gray', ls='-')
        plt.title('KgCO2 x Alimento')
        plt.ylabel('KgCO2', rotation=.5)
        plt.xlabel('Alimento')
        plt.xticks(range(len(self.food_n)), self.food_n)
        plt.bar(self.food_n, np.array(self.w)*self.vector_constant, color='r')
        plt.show()

    def visualize_bar_price(self):
        plt.grid(color='gray', ls='-')
        plt.title('Kg x Price')
        plt.ylabel('Price', rotation=.5)
        plt.xlabel('Alimento')
        plt.xticks(range(len(self.food_n)), self.food_n)
        plt.bar(self.food_n, np.array(self.price)
                * self.vector_constant, color='r')
        plt.show()
