def faltante(lista):
    '''.'''
    i = 0
    while i < len(lista):
        if(len(lista)) == 1:
            return 2
        if i == 0:
            if lista[0] != 1:
                return 1
        if lista[i] != (lista[i-1]+1):
            	return i
        i += 1
    return i+1