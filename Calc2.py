from cv2 import getOptimalNewCameraMatrix
import numpy as np


# Arrays -> weights, price, food_name
# Constante real > 0 -> ceil
class Calc2:
    # w pode ser ndarray ou list
    # ceil > 0 \in R
    def __init__(self, weights, ceil, price, food_name) -> None:
        self.w = weights
        self.ceil = ceil
        self.price = price
        self.food_n = food_name

    def get_better_price_index(self):
        arr = [p*self.ceil/w for w, p in zip(self.w, self.price)]
        index = np.argwhere(arr == np.amax(arr)).flatten().tolist()
        if len(index) == 1:
            return index[0]
        else:
            return np.argwhere(self.w == np.amin(self.w)).flatten().tolist()[0]

    def sol_better_price(self):
        i = self.get_better_price_index()
        return [self.food_n[i], self.ceil/self.w[i], self.price[i], self.w[i]]

    def get_lower_weight_index(self):
        arr = list(self.w)
        index = np.argwhere(arr == np.amin(arr)).flatten().tolist()
        if len(index) == 1:
            return index[0]
        else:
            return np.argwhere(self.price == np.amax(
                self.price)).flatten().tolist()[0]

    def sol_lower_weight(self):
        i = self.get_lower_weight_index()
        return [self.food_n[i], self.ceil/self.w[i], self.price[i], self.w[i]]
