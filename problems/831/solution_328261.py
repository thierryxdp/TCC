def lingua_p(p):
    c = 0
    a = list(p)
    for i in a:
        if i in 'AEIOUaeiou':
            a[c] = i+'p'+i
        c = c + 1
    return a