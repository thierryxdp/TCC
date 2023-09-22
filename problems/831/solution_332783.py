def lingua_p(p):
    a = ''
    j = str.lower(p)
    for l in j:
        if l == (a or e or i or o or u):
            a = l + 'p' + l
        else:
            a = l
    return a