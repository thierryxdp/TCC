def lingua_p(palavra):
    p = ''
    for n in palavra:
        if n in 'aeiouáéíóú':
            p += n+'p'+n
        else:
            p += n
    return p