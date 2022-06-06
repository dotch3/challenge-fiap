from itertools import combinations
import numpy as np
from scipy.optimize import minimize

# Transformação Linear de R^n -> R


class Calc:
    # w pode ser ndarray ou list
    # ceil > 0 \in R
    def __init__(self, weights, ceil) -> None:
        #self.safe_value = 0.1
        self.w = weights
        self.ceil = ceil
        self.sol_dict = None
        self.cart_prod = None

    # Combinação de cada termo
    def comb(self):
        if len(self.w) >= 2:
            # cartesian product combinations
            self.cart_prod = set(combinations(range(len(self.w)), 2))
            return self.cart_prod

    # Regra |x_i-x_{i+1}| + ... + |x_{n-1}-x_n|
    def fun(self, arr):
        self.comb()
        return sum(abs(arr[i[0]]-arr[i[1]]) for i in self.cart_prod)

    # Restrição k_1x_1 + ... + k_nx_n = ceil
    def constraint(self, arr):
        var = - self.ceil
        for i, j in zip(self.w, arr):
            var += i*j
        return var

    def solution(self, method='SLSQP'):
        initial_guess = np.ones(len(self.w))
        cons = {'type': 'eq', 'fun': self.constraint}
        sol_dict = minimize(self.fun, initial_guess,
                            method=method, constraints=cons)
        self.sol_dict = sol_dict
        return self.sol_dict
        # Para pegar o vetor solução: self.solution(method)['x']

    def get_sol_vector(self):
        if len(self.w) == 1:
            return [self.ceil/self.w[0]]
        self.solution()
        return self.sol_dict['x']
