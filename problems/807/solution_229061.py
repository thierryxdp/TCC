"""
"""
def conta_frases(frase):
    f1 = frase.replace('...', '.')
    f2 = f1.replace('!', '.')
    f3 = f2.replace('?', '.')
    return len(f3)