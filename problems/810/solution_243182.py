def inverte(far, oi=0):
    oi = str.replace(str.replace(str.replace(str.replace(str.replace(far, '.', ' '), ',', ' '), '!', ' '), '?', ' '), '-', ' ')
    return str.split(oi)[-1::-1][0]