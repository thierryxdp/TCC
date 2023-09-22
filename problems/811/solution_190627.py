def colchao(medidas,H,L):
    '''função  que recebe as medidas do colchão (a=cm,b=cm,c=cm), a<b<c e as medidas
    da porta, em altura(h) e largura(l) e confere se ele passa pela porta
    medidas-->list
    h---> int ou float
    l---> int ou float
    return-->booleano'''
    
    [A,B,C]= medidas
    A<B<C
    
    if B>H and C>L:
    return "false"

    else:
    return "true"