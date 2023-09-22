def faltante(lista):
    '''descricao'''
    list.sort(lista)
    if lista[0]!=1:
        return 1
    i=1
    n=1
    x=0
    while i<len(lista)+1:
        i=i+1
        if lista[x]!=lista[0]-1 or lista[0]!=lista[0]+1:
            n=lista[0]+1
        return n
    else:
        return len(lista)+1