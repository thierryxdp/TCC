from math import ceil
def carros(pessoas,lugares=5):
    """Dada a quantidade de pessoas, esta função retorna a quantidade de carros
    necessários para o passeio. A quantidade de lugares por carro pode ser
    informada, mas por default, é 5, que é a quantidade de lugares em um carro
    comum. (int, int -> int)"""
    return ceil(pessoas/lugares)