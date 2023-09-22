def colchao(medidas,H,L):
    '''Função que retorna True se o colchão passar pelas portas
    e False caso contrário
    medidas=lista,H=int,L=int->booleano'''
    lista = medidas
    if lista[1]<=H or lista[1]<=L:
        return True
    if lista[2]<=H or lista[2]<=L:
        return True
    else:
        return False