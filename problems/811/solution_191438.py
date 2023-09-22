def colchao(medidas,h,l):
    '''
    Funcao que mostra se é possível o colchão passar pelas portas da casa de João,
    ao retornar um boleano após receber as dimensões, em cm, do colchão que ele pretende
    comprar, em ordem crescente, além da altura e largura da porta a passar
    medidas -> formato [int,int,int], ordem crescente, em cm

    [int,int,int], int, int -> bool

    '''
    if (medidas[2]>h and medidas[2]>l) and (medidas[1]>h and medidas[1]>l):
        return False
    else:
        return True