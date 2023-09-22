from math import ceil
def carros (N,C=5):
    '''retorna a quantidade de carros dados o numero de pessoas(N) e a capacidade do veiculo(C). caso não seja informado a capacidade do veiculo, assume-se que seja capacidade padrao(5)'''
    return ceil(N/C)