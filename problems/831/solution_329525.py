def lingua_p(p):
    pn = ''
    for i in p:
        if i in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            pn = pn + i + 'p' + i
        else:
            pn = pn + i
    return pn