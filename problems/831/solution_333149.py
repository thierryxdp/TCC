def lingua_p(palavra):
    p = ''
    for l in palavra:
        if l.lower in 'aeiouáàãâéèêíìîóòõôúùû':
            p + 'p' + l
        else:
            p + l.lower
    return p