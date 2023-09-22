def inverte(frase):
    caracteres = '-,:;.!?'
    for c in caracteres:
        frase = frase.replace(c, ' ')
    a = frase.split()
    b = a[::-1]
    c = ' '.join(b)
    d = c.lower()
    return d