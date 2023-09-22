def conta_frases(frase):
    ''''''
    f = 0
    if '...' in frase:
        f = f + 1
    if '!' in frase:
        f = f + 1
    if '?' in frase:
        f = f + 1
    if '.' in frase:
        f =f + 1
    return f