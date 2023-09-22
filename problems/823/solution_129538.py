def faltante(lista):
    '''retorna a peça que falta dada uma lista com N elementos numerados sem 
    repetição, list->int'''
    posica=1
    list.sort(lista)
    while posicao in lista:
        posicao+=1
    return posicao