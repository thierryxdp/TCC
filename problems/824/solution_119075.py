def uppCons (f):
    v = ''
    a = []
    for l in f:
            if l == 'a' or l == 'e' or l == 'i' or l == 'o' or  l == 'u':
                v = v + l
            else:
                v = v + (str.upper(l))
    for e in v:
        
        a = a + e
    return v