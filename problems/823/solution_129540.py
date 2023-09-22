def faltante(lista):
    '''retorna a peça que falta dada uma lista com N elementos numerados sem 
    repetição, list->int'''
    posicao=1
    list.sort(lista)
    while posicao in lista:
        posicao=posicao+1
    return posicao