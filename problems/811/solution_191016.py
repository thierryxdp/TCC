def colchao(medidas,H,L):
    '''funcao que recebe uma lista com as dimensoes do colchao e a altura e largura de sia porta
    e retorna se o colchao passa pela porta ou nao. entrada: lista, int, int; saida: bool'''
    if medidas[1] =< H or medidas[1] =< L:
        return True
    elif medidas[2] =< H or medidas[2] =< L:
        return True
    else:
        return False