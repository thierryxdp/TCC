def bolos(A,B,C):
    '''Funcao que recebe o numero de xicaras de farinhas de trigo, o numero de ovos e o numero de colheres de sopa de leite e rerorna quantos bolos e possivel fazer
    int, int, int -> int'''
    trigo = A//2
    ovos = B//3
    leite = C//5
    total = min(trigo,ovos,leite)
    return total