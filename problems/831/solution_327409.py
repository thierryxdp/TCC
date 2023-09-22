def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiou':
            letra += 'p' + letra
        return palavra