def faltante(lista):
    '''descricao'''
    list.sort(lista)
    if lista[0]!=1:
        return 1
    i=0
    n=1
    while i<len(lista)+1:
        i=i+1
        if lista[i]!=lista[i]-1 or lista[i]!=lista[i]+1:
            n=lista[i]+1
        return n
    else:
        return len(lista)+1