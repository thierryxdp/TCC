def lingua_p(palavra):
    i = 0
    for letra in palavra:
        novo = ''
        if letra in 'aeiouAEIOU':
            novo = 'p' + letra
        novapalavra = palavra[:i+1] + novo
    return novapalavra