def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)
    c = 0
    for x in range(len(b)+2):
        if b[c] in 'aeiou':
            list.insert(b, c + 1, 'p' + b[c])   
        c = c + 1
    d = str.join('', b)
    return d