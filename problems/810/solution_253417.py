def inverte(x):
    t = str.replace(x, '.', '')
    t = str.replace(x, '?', '')
    t = str.replace(x, '!', '')
    t = str.replace(x, ',', '')
    t = str.split(t)
    list.reverse(t)
    return t