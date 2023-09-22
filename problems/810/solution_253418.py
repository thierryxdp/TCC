def inverte(x):
    m = str.replace(t, '.', '')
    m = str.replace(m, '?', '')
    m = str.replace(m, '!', '')
    m = str.replace(m, ',', '')
    m = str.split(m)
    list.reverse(m)
    return m