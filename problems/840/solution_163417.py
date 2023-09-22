def farinha(A):
    '''quantidade de bolos baseado na quantidade A de xícaras de farinha'''
    return A//2

def ovos(B):
    '''quantidade de bolos baseado na quantidade B de ovos'''
    return B//3

def leite(C):
    '''quantidade de bolos baseado na quantidade de colheres de leite'''
    return C//5

def bolos(A,B,C):
    '''quantidade real de bolos produzidos com A xicaras de farinha, B ovos e C colheres de leite'''
    return min(farinha(A),ovos(B),leite(C))