def linfua_p(palavra):
    x = ''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóúÁÉÍÓÚ':
            x += letra + 'p' + letra
        else:
            x += letra
    return x