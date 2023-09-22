def lingua_p(palavra):
    p = str.lower(palavra)
    f = ''
    v = 'aeiouáéíóúâôêã'
    for i in p:
        if i in v:
            f += i + 'p' + i
        else:
            f+=i
    return f