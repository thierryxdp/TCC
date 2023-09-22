def lingua_p (pal):
    """Função que recebe uma palavra e a traduz.
"""
    npa = ''
    for x in range (0, len(pal), 1):
        if pal[x] not in 'aáeéiíoôõuú':
            npa = npa + pal[x]
        else:
            npa = npa + pal[x] + 'p' + pal[x]
    return npa