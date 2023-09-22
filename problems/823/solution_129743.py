def faltante(lista):
    '''retorna o número da peça que falta dada uma lista com n número de peças
list -> int'''
    posicao=1
    list.sort(lista)
    while posicao in lista:
        posicao = posicao + 1
    return posicao