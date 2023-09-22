def colchao(medidas,H,L):
    '''Dados as medidas de um colchão e as medidas da porta, retorna se o colchão é capaz de passar na porta ou não
    list,int,int -> bool'''
    if L >= medidas[0] and H >= medidas[1]:
        return True
    else:
        return False