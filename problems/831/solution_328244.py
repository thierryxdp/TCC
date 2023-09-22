def lingua_p(p):
    for i in p:
        if i in 'AEIOUaeiou':
            p = p + 'p' +  i
    return p.lower()