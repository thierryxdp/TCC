def faltante(lista):
	N = len(lista)
    i = 0
    x = 0
    xlista = list(range(1,n+2))
    
    while i < len(xlista):
        if xlista[i] not in lista:
            x = x + xlista[i]
        i = i + 1
    return x