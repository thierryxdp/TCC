def colchao(medidas,H,L):
    '''Retorna True se o colchão passar pela porta e False caso contrário;
    list, int, int -> bool'''
    a,b,c=medidas
    return a<=min(H,L) and b<=max(H,L)