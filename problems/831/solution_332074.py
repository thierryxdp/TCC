def lingua_p(palavra):
    """ """
    traduzido=''
    for letra in palavra:
        if letra in 'aeioouáéíóú':
            traduzido += letra + 'p' + letra
        else:
            traduzido += letra
    return traduzido