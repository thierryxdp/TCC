def faltante(lista):
    '''descricao'''
    list.sort(lista)
    if lista[0]!=1:
        return 1
    i=0
    while i<len(lista):
        i=i+1
        if lista[i]!=lista[i]+1 or lista[i]!=lista[i]-1:
            n=lista[i]
        return n+1