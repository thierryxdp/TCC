def conta_frases(f):
    falt = str.replace(f, '!', '.')
    falt2 = str.replace(falt1, '?', '.')
    qtdf1 = falt2.split('.')
    return len(qtdf1)