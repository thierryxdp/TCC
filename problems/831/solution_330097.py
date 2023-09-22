def lingua_p(palavra):
    nova_palavra = str.lower(palavra)
    for letra in nova_palavra:
        if letra in 'aeiou':
            i = str.find(nova_palavra,letra)
            nova_palavra = nova_palavra[:i+1] + 'p' + nova_palavra[i:]
	return nova_palavra