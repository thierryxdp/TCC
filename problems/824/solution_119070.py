def uppCons (f):
    v = []
    a = []
    for l in f:
            if l == 'a' or l == 'e' or l == 'i' or l == 'o' or  l == 'u':
                v.append([l])
            else:
                v.append([str.upper(l)])
    for e in v:
        a = e + a
    return ' '.join(e)