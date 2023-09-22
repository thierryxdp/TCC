def lingua_p(palavra):
    palavra_traduzida = palavra.lower()
    i = 0
	for letra in palavra_traduzida:
        if letra in 'aeiou':
            palavra_traduzida = palavra_traduzida[1:i:-1] + 'p' + letra + palavra_traduzida[i::]
	return palavra_traduzida