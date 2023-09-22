def lingua_p(palavra):
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            i = str.find(palavra,letra)
            nova_palavra = palavra[:i+1] + 'p' + palavra[i:]
	return nova_palavra