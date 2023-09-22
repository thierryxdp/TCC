def lingua_p(palavra):
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            i = str.index(palavra,letra)
            palavra = palavra[:i+1]+'p'+palavra[i:]
	return palavra