def faltante(pecas):
    '''Função que dada uma lista com um numero x de peças - 1, retorna a peça faltando.
    peca -> list
    return -> int'''
    lista = pecas
    peca = 1
    
    while peca < len(lista):
        if peca in lista:
            peca+=1
    return peca