def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)   
    c = 0
    for x in range(len(b)):
        if b[x] in 'aeiouáéóú':
            list.insert(b, x + 1, 'p' + b[c])   
        c = c + 1
    f = str.join('', b)
    return f