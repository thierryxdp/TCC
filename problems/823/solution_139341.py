def faltante(lista):
    '''Essa função retornar o numero da peça faltante em relação as peças enumeradas na lista,
    list->int'''
    list.sort(lista)
    i=0
    maior=max(lista)
    faltante=list(range(1,maior+1))
    while i<len(lista):
        if faltante[i]!=lista[i]:
           return faltante[i]
        i+=1
        lista[i]+=1
    return maior+1