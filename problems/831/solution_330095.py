def lingua_p(palavra):
    nova_palavra = str.lower(palavra)
    for letra in nova_palavra:
        if letra in 'aeiou':
            i = str.find(palavra,letra)
            nova_palavra = palavra[:i+1] + 'p' + palavra[i:]
	return nova_palavra