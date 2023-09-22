def lingua_p(palavra):
    palavra = str.lower(palavra)
    lista = []
    for letra in palavra:
        if letra in 'aeiou':
            i = str.find(palavra,letra)
            palavra = palavra[:i] + 'p' + palavra[i:]
	return palavra