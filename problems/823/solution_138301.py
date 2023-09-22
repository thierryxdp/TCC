def faltante(lista):
    lista.sort()
    i = 1
    n = len(lista) - 1
    while i < n:
        if i not in lista:
            # é a peça que falta
            return i
        
        i += 1
	
    return i