def bolos(A,B,C):
    '''calcula e retorna a quantidade maxima de bolos possiveis de serem feitos;
    int,int,int->int'''
    xicara=A//2
    ovos=B//3
    colheres=C//5
    return min(xicara,ovos,colheres)