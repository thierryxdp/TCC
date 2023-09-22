def faltante(lista):
    contador = -1
    x = len(lista) + 1
    for n in range(x):
        contador +=1
        if contador < x:
        	if n+1 != lista[contador]:
            	return n+1