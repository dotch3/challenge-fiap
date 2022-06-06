import numpy as np

from Calc import Calc
from Calc2 import Calc2
from Report import Report
from Report2 import Report2

# var
food_name = ['arroz', 'batata', 'nozes']
price = [7, 5, 7]
w = [3.6, 0.2, .3]
teto = 1000


# Teste opc1
c2 = Calc2(w, teto, price, food_name)
print(c2.sol_better_price())
print(c2.sol_lower_weight())
# View opc1
x = c2.sol_better_price()
print(x)
rp = Report2(x[0], x[1], x[2], x[3])
rp.visualize_pollution()
rp.visualize_price()
x = c2.sol_lower_weight()
rp = Report2(x[0], x[1], x[2], x[3])
rp.visualize_pollution()
rp.visualize_price()


# *--------------------------------*
# Teste opc2
c1 = Calc(w, ceil=teto)
print(c1.get_sol_vector())
# View opc2
# 3d
rp = Report(food_name, w, c1.get_sol_vector(), price)
rp.visualize_bar_pollution()
rp.visualize_bar_price()
rp.visualize_vector()

# 1d
a = Calc([1], teto)
print(a.get_sol_vector())
rp = Report('abc', [1], a.get_sol_vector(), [2])
rp.visualize_bar_pollution()
rp.visualize_bar_price()
rp.visualize_vector()
