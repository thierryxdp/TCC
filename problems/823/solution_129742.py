def faltante(lista):
    '''retorna o número da peça que falta dada uma lista com n número de peças
list -> int'''
    posição=1
    list.sort(lista)
    while posição in lista:
        posição = posição + 1
    return posição