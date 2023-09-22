def lingua_p(palavra):
    for letra in palavra:
    	novo = ''
        if letra in 'aeiouAEIOU':
            novo = 'p' + letra
        novapalavra = letra + novo
    return novapalavra