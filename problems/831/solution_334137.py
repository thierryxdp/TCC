def lingua_p(palavra):
    'pega uma palavra e retorn uma nova que substituiu as vogais por p'
    'string---string'
    for letra in palavra.lower():
        if letra in'áéíóúaeiou':
            ppalvra+=letra+'p'+letra
        else :
            ppalavra+=letra
    return ppalavra