def faltante(lista):
    list.sort(lista)
    n=0
    while n < len (lista):
        if lista[n]+1 != lista[n+1]:
            resposta = int((lista[n] + lista [n+1])/2)
        n += 1
    if lista[n]+1 == lista[n+1]:
        resposta = lista[-1] + 1  
	return resposta