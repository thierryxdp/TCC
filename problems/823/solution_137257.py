def faltante(lista):
    '''Retorna o número da peça faltante
    	list -> int'''
    list.sort(lista)
    i = 1
    while i <= len(lista):
        if i != lista[i-1]:
            return i
        i = i + 1
    return i + 1