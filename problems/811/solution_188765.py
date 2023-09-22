def colchao(medidas,H,L):
    '''Função que recebe uma lista de 3 elementos contendo as medidas
    do colchão, a altura H e a largura L das portas de sua casa. A função
    retorna True se o colchão passar pelas portas e False se o colchão não passar.
    lista,int,int->bool'''
    if medidas[1]<=H or medidas[2]<=L:
        return True
    else:
        return False