def bolos(a,b,c):
    '''retorna a quantidade de bolos que João consegue fazer
    dados os ingredientes: (a)xícaras de farinha, (b)ovos e
    (c)colheres de sopa de leite'''
    if a<2 or b<3 or c<5:
        return 0
    else:
        return int(a/2) % int(b/3) % int(c/5)