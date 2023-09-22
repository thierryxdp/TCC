def bolos(a,b,c):
    '''Função que determina a quantidade máxima de bolos que pode ser feita
    de acordo com os indigredientes disponíveis, onde:
    a: xícaras de farinha de trigo
    b: ovos
    c: colheres de sopa de leite
    int,int,int -> int'''
    farinha = a//2
    ovos = b//3
    leite = c//5
    return min(farinha,ovos,leite)