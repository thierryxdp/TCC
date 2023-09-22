def colchao(medidas,H,L):
    '''
    funcao que recebe uma lista e altura h e largura l da porta
    e retorna true caso o colchao passe pela porta ou
    false se ele n passar
    list,int,int -> bol
    '''
    
    if medidas[0] <= H or medidas[1] =< L:
        return True
    elif medidas[1] <= H or medidas[0] =< L:
        return True
    else:
        return False