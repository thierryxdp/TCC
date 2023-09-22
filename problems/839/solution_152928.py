import math
def carros (num_pessoas, capacidade= 5):
    '''funcao que calcula o numero exato de carros necessarios para a viagem dado o numero total de pessoas e a capacidade maxima vo veiculo;
    int, int -> int'''
    return math.ceil(num_pessoas / capacidade)