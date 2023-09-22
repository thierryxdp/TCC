def lingua_p(lista):
    '''Esta e a funcao que recebe uma palavra e retorna-a traduzida
na lingua do P. Ou seja, quando apos cada vogal da palavra original
e inserida a sequencia de letras p mais a vogal original'''
    lista.lower()
    vogal='aeiou'
    nova_lista = []
	for item in lista:
        if letra==vogal:
            nova_lista.append(letra+"p"+letra)
    return lista