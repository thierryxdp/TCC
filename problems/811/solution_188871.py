def colchao(medidas,H,L):
    '''
    funcao que recebe uma lista e altura h e largura l da porta
    e retorna true caso o colchao passe pela porta ou
    false se ele n passar
    list,int,int -> bol
    '''
    
    if medidas[0] <= H:
        return True
    elif medidas[1] <= H:
        return True
    else:
        return False