def uppCons (f):
    v = ''
    a = []
    for l in f:
            if l == 'ã' or l == 'ó' or l == 'ú' or l == 'a' or l == 'e' or l == 'i' or l == 'o' or  l == 'u':
                v = v + l
            else:
                v = v + (str.upper(l))

    return v