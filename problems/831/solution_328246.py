def lingua_p(p):
    for i in p:
        if i in 'AEIOUaeiou':
            p.replace(i,'a')
    return p.lower()