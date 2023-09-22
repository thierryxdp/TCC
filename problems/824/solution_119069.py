def uppCons (f):
    v = []
    for l in f:
            if l == 'a' or l == 'e' or l == 'i' or l == 'o' or  l == 'u':
                v.append([l])
            else:
                v.append([str.upper(l)])
    return  v