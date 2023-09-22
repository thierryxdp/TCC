def lingua_p(palavra:str)->str:
    palavra = palavra.lower()
    aux = ''
    for i in palavra:
        if i in 'aeiou':
            aux += i + 'p' + i
        else:
            aux += i
	return aux