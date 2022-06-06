from matplotlib import pyplot as plt
import numpy as np


class Report2:
    def __init__(self, food_name, kg, price, weight) -> None:
        self.food_n = food_name
        self.kg = kg
        self.price = price
        self.w = weight
        self.figure = plt.figure(dpi=150)

    def visualize_price(self):
        plt.grid(color='gray', ls='-')
        plt.title('KG x CO2')
        plt.ylabel('CO2', rotation=.5)
        plt.xlabel(f'Kg ({self.food_n.title()})')
        x = np.linspace(0, int(self.kg), int(self.kg)*3)
        y = self.w*x
        plt.plot(x, y, 'b')
        plt.show()

    def visualize_pollution(self):
        plt.grid(color='gray', ls='-')
        plt.title('KG x Price')
        plt.ylabel('Price', rotation=.5)
        plt.xlabel(f'Kg ({self.food_n.title()})')
        x = np.linspace(0, int(self.kg), int(self.kg)*3)
        y = self.price*x
        plt.plot(x, y, 'b')
        plt.show()
