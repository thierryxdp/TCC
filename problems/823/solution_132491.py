def faltante(lista):
    '''A função descobre qual número está faltando da peça
    está faltando dado uma lista com N números
    lista -> int'''
    
    i = 0
    x = list(range(lista[0],lista[-1]))
    t = []
    
    while len(lista) > i:
        if lista[i] in x:
            list.append(t, lista[i])
        i = i + 1
    return t[0]