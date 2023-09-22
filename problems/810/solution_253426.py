def inverte(texto):
    e = ' '
    t = str.replace(texto, '.', '')
    t = str.replace(t, '?', '')
    t = str.replace(t, '!', '')
    t = str.replace(t, ',', '')
    t = str.split(t)
    list.reverse(t)
    t = str(e.join(t))
    return str.lower(t)