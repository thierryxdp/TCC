def colchao(medidas,H,L):
    '''Essa função recebe como 3 parâmentros de entrada correspondente as informações
    do colchão e da porta, e retorna True caso o colchão passe pela 
    porta ou False caso contrário list-bool>'''
    if medidas[0]<=H and medidas[1]<=L:
        return True
    else:
        False