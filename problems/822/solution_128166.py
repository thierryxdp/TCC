def repetidos(lista):
    contador = 0
    proximo = 0
    while proximo < len(lista):
      		if lista[proximo] == lista[proximo+1]:
            	contador = contador + 1
    proximo = proximo + 1
    return contador