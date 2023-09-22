def lingua_p(lista):
    '''Esta e a funcao que recebe uma palavra e retorna-a traduzida
na lingua do P. Ou seja, quando apos cada vogal da palavra original
e inserida a sequencia de letras p mais a vogal original'''
    i=0
    lista.lower()
    vogal='aeiou'
	vogal[i]
	for item in lista:
        if item==vogal:
            lista.replace(item,item+"p"+item)
    i+=1
	return lista