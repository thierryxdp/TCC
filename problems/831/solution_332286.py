def lingua_p(palavra):
    for letra in palavra:
        i = palavra.index(letra)
        if letra in 'aeiouAEIOU':
            novo = 'p' + letra
        palavra = palavra[:i+1] + novo
    return palavra