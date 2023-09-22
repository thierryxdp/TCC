def inverte(texto):
    e = ''
    t = str.replace(x, '.', '')
    t = str.replace(t, '?', '')
    t = str.replace(t, '!', '')
    t = str.replace(t, ',', '')
    t = str.split(t)
    list.reverse(t)
    t = [e.join(t)]
    return t