def carros(pessoas,capacidade=4):
    """calcula o numero de carros necessarios para fazer uma viagem dados o numero de pessoas e a capacidade 
    de cada carro, considerando que todos eles tem capacidade igual e caso nao for dado sua capacidade sera
    igual a 5"""
    return pessoas%capacidade