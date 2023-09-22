def lingua_p(palavra):
    x = ''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            x += letra+'p'+letra
        else:
            x += letra
    return str.lower(x)