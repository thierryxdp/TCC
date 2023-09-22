def colchao(medidas,h,l):
    '''função que dadas as dimensões de um colchão em uma lista,A,B,C e a altura(h) da porta e a largura(l) da mesma, retorna se o colchão passa ou não por essa porta; lista, int, int -> bool'''
    if lista[0]<=h and lista[1]<=l:
        return True
    if lista[0]<=l and lista[1]<=h:
        return True
    else:
        return False