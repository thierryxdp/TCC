def lingua_p(p):
    a = p[:]
    for i in p:
        if i in 'AEIOUaeiou':
            a = a.replace(i,'a')
    return a.lower()