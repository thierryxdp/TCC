def faltante(pecas):
    pecas.sort()
    contador = 0
    #peca = -1
    while (contador < len(pecas)):
		if (pecas[contador] == (contador + 1) and contador!=len(pecas)-1):
            contador+=1
		elif contador==len(pecas)-1:
            return contador+2
        else:
            return contador