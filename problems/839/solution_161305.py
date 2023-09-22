def carros(x,y=5):
    """ calcula a quantidade de carros necessários para transportar
    um número 'x' de pessoas em um veículo com capacidade para
    'y' passageiros; OBS.: caso não seja adicionada a capacidade
    será dada como 5; int , int --> int"""
    return math.ceil(x/y)