def lingua_p(palavra):
    traduzido = ''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            traduzido += letra + 'p' + letra
        else:
            traduzido += letra
    return traduzido