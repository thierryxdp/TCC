def lingua_p(p):
    pn = ''
    for i in p:
        if i in 'aeiouAEIOU':
            pn = pn + i + 'p'
        else:
            pn = pn + i
    return pn