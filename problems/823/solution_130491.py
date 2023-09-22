def faltante(lista):
	'''Retorna o numero da peça faltante do quebra cabeças''' 
    N = len(lista)
    i = 0
    x = 0
    xlista = list(range(1,N+2))
    
    while i < len(xlista):
        if xlista[i] not in lista:
            x = x + xlista[i]
        i = i + 1
    return x