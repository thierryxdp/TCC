def lingua_p(p):
    a = ''
    j = str.lower(p)
    for l in j:
        if l == ('a' or 'e' or 'i' or 'o' or 'u' or 'á' or 'é' or 'í' or 'ó' or 'ú'):
            a = a + (l + 'p' + l)
        else:
            a = a + l
    return a