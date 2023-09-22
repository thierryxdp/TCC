def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)
    t = list.count('a', b) + list.count('e', b) + list.count('i', b) + list.count('o', b) + list.count('u', b)
    c = 0
    for x in range(len(b)+t):
        if b[c] in 'aeiou':
            list.insert(b, c + 1, 'p' + b[c])   
        c = c + 1
    d = str.join('', b)
    return d