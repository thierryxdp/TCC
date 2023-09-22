def faltante(pecas):
    pecas.sort()
    contador = 0
    #peca = -1
    while (contador < len(pecas)):
        if (pecas[contador] != (contador + 1)):
            contador+=1
        
	return contador