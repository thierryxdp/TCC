def lingua_p(p):
    a = ''
    j = str.lower(p)
    for l in j:
        if (l == 'a') or (l == 'e') or (l == 'i') or (l == 'o') or (l == 'u'):
            a = a + (l + 'p' + l)
    return a