def bolo(A,B,C):
    '''Funcao que dados A xicaras de farinha de trigo, B ovos
    e C colheres de sopa de leite, retorna a quantidade maxima
    de bolos inteiros possiveis de serem feitas dados as 
    quantidades de cada ingrediente disponiveis;
    entrada: int, int, int
    saida: int'''
    farinha=A//2
    ovos=B//3
    leite=C//5
    return min(farinha, ovos, leite)