def colchao(medidas,H,L):
    '''Retorna se é possível passar um colchão por uma porta com medidas HxL
    medidas = medidas do colchão
    list , int , int -> bool'''
    a=min(medidas)
    medidas.remove(min(medidas))
    b=min(medidas)
    if a<=min(H,L) and b<=max(H,L):
        return True
    else:
        return False