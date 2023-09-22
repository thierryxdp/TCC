def colchao(medidas,H,L):
    ''' Função que informa se é possivel passar por uma porta de altura H e largura
    L um colchão de dimenções A x B x C repressentadas na lista medidas. Sendo A<B<C
    e todas medidas são inteiras. list, int, int -> boolean.'''
    x=medidas[1]
    y=medidas[2]
    if ((H>=x and L>=y)or(H>=y and L>=x)):
        return True
    else:
        return False