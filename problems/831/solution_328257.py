def lingua_p(p):
    for i in p:
        if i in 'AEIOUaeiou':
            a = p.replace(i,i+'p'+i)
            b = a.replace(i,i+'p'+i)
    return b.lower()