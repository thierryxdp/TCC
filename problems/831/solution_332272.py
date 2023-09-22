def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavra[palavra.index(letra)] = letra + 'p' + letra
    return palavra