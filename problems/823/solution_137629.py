def faltante(numeros):
    '''função que retorna o número inteiro que não está na lista, dado a lista de números;list->int'''
    i=0
    faltante=0
    while i<len([list.sort(numeros)]):
        if list.sort(numeros)[i]!=list.sort(numeros)[i+1]-1:
            faltante=faltante+(i+2)
        i=i+1
    return faltante