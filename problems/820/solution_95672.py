def posLetra(frase, letra, numero):
    '''função que dada uma frase uma letra e um numero que indica a 
    ocorrência da letra na frase e retorna a posição que a letra 
    aparece na frase'''
    contador = 0
    vezes = 0
    aparicoes = frase.count(letra)
    if aparicoes < numero:
    	return -1
    else:
    	while vezes != numero:
        	if frase[contador] == letra:
            	vezes = vezes + 1
        	contador = contador + 1
	return contador - 1