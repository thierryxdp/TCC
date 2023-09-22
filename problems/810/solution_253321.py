def inverte(texto):
    sempontos = ''
    for c in texto:
        if c.isalpha() or c == ' ':
            sempontos += c
            sempontos + ' '
    return sempontos