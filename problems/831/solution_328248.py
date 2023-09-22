def lingua_p(p):
    for i in p:
        if i in 'AEIOUaeiou':
            a = p.replace(i,'a')
    return a.lower()