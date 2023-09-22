def posLetra(frase, letra, numero):
    '''função que dada uma frase uma letra e um numero que indica a 
    ocorrência da letra na frase e retorna a posição que a letra 
    aparece na frase'''
    contador = 0
    vezes = 0
    while contador < len(frase):
        aparicoes = frase(letra)
        if aparicoes < numero:
            return -1
        elif frase[contador] == letra:
            vezes = vezes + 1
        else:
            vezes += 0
        contador = contador + 1
	return vezes