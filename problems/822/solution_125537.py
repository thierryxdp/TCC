def repetidos(lista):
    ''' Recebe uma lista e conta quantas vezes o elemento dessa lista é igual ao seu anterior
    list->int'''
    i=1
    vezes_que_ocorre=0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            vezes_que_ocorre= vezes_que_ocorre + 1
        i=i+1
    return vezes_que_ocorre