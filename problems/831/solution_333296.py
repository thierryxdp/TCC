def lingua_p(palavra):
    traduzindo_p = []
    contador = 0
    for letra in list(palavra):
        if letra in'aeiouáéíóú':
            traduzindo_p.append(letra + 'p' + letra)
        else:
            traduzindo_p.append(letra)
    return ''.join(traduzindo_p)