def inverte(frase):
    for char in ".!?,":
        frase = frase.replace(char, '')
        frase = frase.replace('-', ' ')
    z = str.split(frase, ' ')
    y = z[::-1]
    x = str.join(' ', y)
    return str.lower(x)