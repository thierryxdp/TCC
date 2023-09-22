def lingua_p(palavra):
    novapalavra = ''
    for letra in palavra:
    	novo = ''
        if letra in 'aeiouAEIOU':
            novo = 'p' + letra
        novapalavra = str.lower(novapalavra + letra + novo)
    return novapalavra