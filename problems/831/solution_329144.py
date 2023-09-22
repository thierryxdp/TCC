def lingua_p(palavra):
    """Recebe uma palavra e a coloca na língua do p;
	str -> str"""
    p = ''
    for n in palavra:
        if n in 'aeiouáéíóú':
            p += n+'p'+n
        else:
            p += n
    return p