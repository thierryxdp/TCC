def carros(pessoas, capveiculos=5):
    '''Funcao que retorna o numero de carros iguais necessarios
    para transportar um dado numero de pessoas e a capacidade 
    dos veiculos que, se nao informado, sera igual a 5;
    entrada: int, int
    saida: int'''
    numcarros = pessoas / capveiculos
    if pessoas % capveiculos != 0:
        return numcarros+1
    else:
        return numcarros