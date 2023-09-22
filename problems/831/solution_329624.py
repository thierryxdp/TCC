def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)
    c = 0
    for x in range(len(b)):
        if b[c] in 'aeiou':
            list.insert(b, c + 1, 'p' + b[c])
    d = str.join('', b)    
    c = c + 1      
    return d