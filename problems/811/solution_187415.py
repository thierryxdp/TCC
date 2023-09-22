def colchao(medidas,h,l):
    '''Retorna True se for possível o colchão passar pela porta
    e False se não for possível
    list, int, int -> bool'''
    if medidas[1]<=h:
        return True
    if medidas[1]>=h and medidas[2]<l:
        return True
    else:
        return False