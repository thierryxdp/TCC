def inverte(texto):
    m = str.replace(texto, '.', '')
    m = str.replace(m, '?', '')
    m = str.replace(m, '!', '')
    m = str.replace(m, ',', '')
    m = str.split(m)
    list.reverse(m)
    return m