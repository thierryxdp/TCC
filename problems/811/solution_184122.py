def colchao(medidas,H,L):
    '''Dados as medidas de um colchão em ordem crescente, a altura e largura da porta, retorna se o colchao passa pela porta.
    list, int, int -> bool'''
    if medidas[1] > H:
        return False
    else:
        return True