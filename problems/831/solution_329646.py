def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)
    d = b
    c = 0
    for x in range(len(b)):
        if d[c] in 'aeiou':
            list.insert(b, c + 1, 'p' + b[c])   
        c = c + 1
    d = str.join('', b)
    return d