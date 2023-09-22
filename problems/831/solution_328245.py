def lingua_p(p):
    for i in p:
        if i in 'AEIOUaeiou':
            p.replace(i,i+'p'+i)
    return p.lower()