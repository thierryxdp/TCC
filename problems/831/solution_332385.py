def lingua_p(palavra):
    novapalvra = ''
    for letra in palavra:
    	novo = ''
        if letra in 'aeiouAEIOU':
            novo = 'p' + letra
        novapalavra = novapalavra + letra + novo
    return novapalavra