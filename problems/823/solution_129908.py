def faltante(lista):
    proximo = 0
    while proximo<len(lista):
        completo = list(range(1,len(lista)+2))
        soma1 = sum(completo)
        soma2 = sum(lista)
    	return soma1-soma2