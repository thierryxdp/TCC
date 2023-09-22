def quantidade(A,B,C):
    '''retorna a quantidade minima de uma receita'''
    return (A//2),(B//3),(C//5)	

def bolos(A,B,C):
    'retorna a quantidade maxima de bolos a partir de uma receita'
    return min(quantidade(A,B,C))