def lingua_p(string):
	str.lower(string)
    tamanho = len(string)
    palavra = string
    for indice in list(range(tamanho)):
        letra = string[indice]
        if letra in 'aeiou':
            palavra = str.join(str.split(string)[0] + letra + 'p' + letra + str.split(string)[1]
	return palavra