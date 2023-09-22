from math import floor
def bolos(a=2, b=3, c=5):
    ''' função que calcula e retorna a quantidade de bolos que pode ser feita por João, tendo em conta a quantidade mínima de ingredientes para que um cada bolo possa ser feito: 2 xícaras, 3 ovos e 5 colheres. '''
    return floor(a+b+c)//(2+3+5)