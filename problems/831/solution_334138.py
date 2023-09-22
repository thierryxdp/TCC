def lingua_p(palavra):
    'pega uma palavra e retorn uma nova que substituiu as vogais por p'
    'string---string'
    ppalavra= ''
    for letra in palavra.lower():
        if letra in'áéíóúaeiou':
            ppalavra+=letra+'p'+letra
        else :
            ppalavra+=letra
    return ppalavra