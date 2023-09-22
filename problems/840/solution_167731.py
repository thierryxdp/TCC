def bolos(a,b,c):
    '''retorna a quantidade de bolos que João consegue fazer
    dados os ingredientes: (a)xícaras de farinha, (b)ovos e
    (c)colheres de sopa de leite'''
    if a<2 or b<3 or c<5:
        return 0
    else:
        return round(a/2) + round(b/3) + round(c/5)