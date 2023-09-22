from math import ceil
def carros(pessoas,capacidade=5):
    """calcula e retorna o numero de carros necessarios para um grupo de amigos conseguirem realizarem uma viagem, dado os valores de entrada de numeros de pessoas e a capacidade dos veiculos. Caso nao seja dado a capacidade do veiculo, sera utilizada a capacidade tradicional, ou seja, de cinco pessoas;
    int, int->int
    return ceil(pessoas,capacidade)