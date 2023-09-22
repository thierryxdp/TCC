def uppCons(f):
    n = ''
    vogal = 'aeiouáéíóúâêôã'
    for i in f:
        if i in vogal:
            n += i
        else:
            n += str.upper(i)
    return n