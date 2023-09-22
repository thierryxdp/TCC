def colchao(lista,H,L):
    """ Função que retorna se o colchão passa pela porta. Retornará True se passar e False se não. lista,int,int -> bool"""
    list.sort(lista)
    if H > L:
        return lista[0] <= L and lista[1] <= H
    else:
        return lista[0] <= H and lista[1] <= L