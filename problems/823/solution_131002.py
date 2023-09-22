def faltante(lista):
    '''Função que identifica e retorna o número da peça que esta faltando. list->int'''
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+1
    c=0
    falta=0
    while c<len(lista)-1:
        if lista[c+1]-lista[c]>1:
            falta=falta+lista[c]+1
        c=c+1
    return falta