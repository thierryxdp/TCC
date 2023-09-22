def faltante(lista):
    '''.'''
    i = 0
    while i < len(lista):
        if i == 0:
            if lista[0] != 1:
                return 1
        else:
            if lista[i] != (lista[i-1]+1):
            	return i
        i += 1