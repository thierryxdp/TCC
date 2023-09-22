def conta_frases(f):
    falt = str.replace(f, '!', '?', '-', ';', '.')
    qtdf1 = falt.split('.')
    return len(qtdf1)