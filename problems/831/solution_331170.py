def lingua_p(lista):
    '''Esta e a funcao que recebe uma palavra e retorna-a traduzida
na lingua do P. Ou seja, quando apos cada vogal da palavra original
e inserida a sequencia de letras p mais a vogal original'''
    lista.lower()
	vogal='aeiou'
	for item in lista:
        if letra==vogal:
            lista.replace(letra,letra+"p" + letra)
	return lista