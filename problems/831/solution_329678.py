def lingua_p(palavra):
    a = str.lower(palavra)
    b = list(a)
    t = list.count(b, 'a') + list.count(b, 'e') + list.count(b, 'i') + list.count(b, 'o') + list.count(b, 'u') + list.count(b, 'é') + list.count(b, 'á') + list.count(b, 'ó') 
    c = 0
    for x in range(len(b) + t):
        if b[c] in 'aeiouáéíóú':
            list.insert(b, c + 1, 'p' + b[c])   
        c = c + 1
    d = str.join('', b)
    return d