def faltante(pecas):
    '''Função que dada uma lista com um numero x de peças - 1, retorna a peça faltando.
    peca -> list
    return -> int'''
    lista = pecas
    peca = 1
    i = 0
    
    while peca < len(lista):
        if peca == lista[i]:
            peca+= 1
        i+=1
        
        if peca != lista[i]:
            return peca + 1
    return peca