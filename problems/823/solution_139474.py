def faltante(n):
    '''A funcao recebe uma lista com a enumeracao de pecas e retorna qual das pecas esta faltando
list->int'''
    lista=list(range(1,len(n)+1))
    ordem=0
    falta=[]
    while ordem<len(n)+1:
        if n[ordem] not in lista:
            falta.append(lista[ordem])
        ordem=ordem+1
    return falta[0]