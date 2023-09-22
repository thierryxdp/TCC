def colchao(medidas,H,L):
    '''uma funcao que retorna se é true ou false se o colchao passa pela medidas das portas'''
    '''list->list'''
    if medidas [1]<= H:
        return True
    if medidas [1]<=L:
        return True
    else:
        return False