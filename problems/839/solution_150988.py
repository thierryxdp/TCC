from math import
def carros(p,c=5):
    """calcula e retorna o numero de carros necessarios para um grupo de amigos conseguirem realizarem uma viagem, dado os valores de entrada dos numeros de pessoas(p) e da capacidade dos veiculos(c), caso nao seja dado a capacidade do veiculo, sera utilizada a capacidade tradicional, ou seja, de cinco pessoas;
    int, int->int"""
    return math.ceil(p,c)