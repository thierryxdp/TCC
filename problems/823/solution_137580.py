def faltante(pecas):
    '''Função que dada uma lista com um numero x de peças - 1, retorna a peça faltando.
    peca -> list
    return -> int'''
    organizada = pecas.sort()
    peca = 1
    
    while peca in organizada:
        if peca in organizada:
            peca += 1
            else:
                return peca