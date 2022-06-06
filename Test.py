from Info import get_data
from Calc import Calc
from Calc2 import Calc2

df = get_data(r'Food_Production.csv')

# Pegando apenas 5 linhas de cada coluna
test_df = df[['food_name', 'weight', 'prices']][:5]
print(test_df)


# Criar menu ou interface que pegue:
# peso do produto, teto, price, food_name
# ao requisitar ao usuario


menu = '''Maximizar:
<1> - Lucro
<2> - Igualdade de produção
<3> - Alimento que gera menos poluição
Opção:'''
opts = range(1, 4)

teto = 100
while True:
    print(menu)
    user_input = int(input(''))
    if user_input not in opts:
        pass
    elif user_input == 1:
        a = Calc2(test_df['weight'], teto,
                  test_df['prices'], test_df['food_name']).sol_better_price()
        print('Name - Kg - Price - Weight')
        print(a)
    elif user_input == 2:
        b = Calc(test_df['weight'], teto).get_sol_vector()
        print('Name - Kg - Weight - Price')
        for n, k, w, p in zip(test_df['food_name'], b, test_df['weight'], test_df['prices']):
            print(n, k, w, p,)
    elif user_input == 3:
        c = Calc2(test_df['weight'], teto,
                  test_df['prices'], test_df['food_name']).sol_lower_weight()
        print('Name - Kg - Price - Weight')
        print(c)
