def faltante(lista):
    '''função que recebe uma lista com a numeração das peças e retorna a peça faltante. list -> int'''
    faltando =[]
    for i in range(1,len(lista)+2):
        if i not in lista:
            faltando.append(i)
    return faltando [0]