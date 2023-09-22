def faltante(lista):
    list.sort(lista)
    n=0
    while n < len (lista):
        if lista[n]+1 != lista[n+1]:
            return int((lista[n] + lista [n+1])/2)
        else: 
            return lista[n] + 1
        n += 1
        
	return