def inverte(far, puff=0):
    puff = str.replace(str.replace(str.replace(str.replace(str.replace(far, '.', ' '), ',', ' '), '!', ' '), '?', ' '), '-', ' ')
    return list.reverse(puff)