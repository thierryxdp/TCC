def inverte(frase):
    '''função que recebe uma frase e devolve esta frase em ordem invertida
    removendo sua pontuação e letras maiúsculas'''
    pontos = ['-',',',':',';','.','?','!','...']
	for i in range(len(pontos)):
		frase = frase.replace(pontos[i], ' ')
    frase = frase.lower()
    lista_palavras = frase.split(' ')
    lista_palavras.reverse()
    frase = ' '.join(lista_palavras)
    frase.removeprefix(' ')
    return frase