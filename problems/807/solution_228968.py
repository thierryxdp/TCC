def conta_frases(f):
    qtdf1 = f.split('.', '?', '!')
    qtdf2 = f.split('?')
    qtdf3 = f.split('!')
    return len(qtdf1) + len(qtdf2) + len(qtdf3)