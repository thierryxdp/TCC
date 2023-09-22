def colchao(lista,h,l):
    """A função que calcula se um colchao de dimensoes
    [a,b,c] passa por uma porta de altura h e largura l.
    lista(float,float,float), float, float --> boolean"""
    if(lista[1]<=h and lista[0]<=l):
        return 1==1
    if(lista[1]<=l and lista[0]<=h):
        return 1==1
    else:
        return 1>2