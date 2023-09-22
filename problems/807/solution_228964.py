def conta_frases(f):
    qtdf = f.split('.', '!')
    qtdf2 = f.split('...', '?')
    qtdf3 = f.split(';', '-')
    return len(qtdf) + len(qtdf2) + len(qtdf3)