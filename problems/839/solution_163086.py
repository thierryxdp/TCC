import math
def carros(pessoas, capveiculos=5):
    '''Funcao que retorna o numero de carros iguais necessarios
    para transportar um dado numero de pessoas e a capacidade 
    dos veiculos que, se nao informado, sera igual a 5;
    entrada: int, int
    saida: int'''
    numcarros = math.ceil(pessoas / capveiculos)
        return numcarros