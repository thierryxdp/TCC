def bolos(a,b,c):
    '''Calcula a quantidade maxima de bolos que da para serem
    feitos. Dados: 
    a=xic.farinha trigo;
    b=ovos;
    c=colheres leite
    int, int, int ->int'''
    if (a//2) and (b//3) and (c//5) >=1:
        return min((a//2),(b//3),(c//5))
    else:
        return 0