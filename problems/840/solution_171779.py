def bolos(a,b,c):
    '''
    dados a quantidade de ingredientes 
    de farinha, ovos e leite, a função retorna 
    a quantidade de bolos que se consegue fazer 
    de acordo as respectivas proporções dos ingredientes.
    int -->int
    '''
    x = (a//2,b//3,c//5)
    return min(x)