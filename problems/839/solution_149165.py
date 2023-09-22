from math import ceil
def carros(pessoas,capacidade=5):
    """Retorna a quantidade de carros necessários para fazer uma viagem com o total de pessoas como o primeiro valor de entrada e a capacidade de passageiros do carro como o segundo valor de entrada;
    int,int->int"""
    return ceil(pessoas/capacidade)