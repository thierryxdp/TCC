def colchao(medidas,H,L):
    '''A partir das medidas do colchao e da altura H e largura L da porta
    retorna true se é possivel passar o colchao pela porta
    list[int,int,int],int,int -> bool'''
    a,b,c = medidas
    if a<=b and a<=c:
        if b<c:
            return a<=L and b<=H
        elif c<=b:
            return a<=l and c<=H
    if b<a and b<=c:
        if a<c:
            return b<=L and a<=H
        elif c<=a:
            return b<=L and c<=H
    if c<a and c<b:
        if a<b:
            return c<=L and a<=H
        elif b<=a:
            return c<=L and b<=H