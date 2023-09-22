def lingua_p(p):
    a = ''
    p1 = p.lower
    for l in p1:
        if l == (a or e or i or o or u):
            a = l + 'p' + l
        else:
            a = l
    return a