def conta_frases(f):
    falt = str.replace(f, '!', '.', 999)
    qtdf1 = falt.split('.', '?')
    return len(qtdf1)