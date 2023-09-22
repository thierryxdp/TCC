#Bolos
def bolos(A,B,C):
    farinha=A//2
    ovos=B//3
    leite=C//5
    '''Função que calcula e retorna a quantidade máxima 
    de bolos que pode ser feita.
    int,int=>int'''
    return min(farinha, ovos, leite)