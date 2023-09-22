def conta_frases(txt):
    """Conta o número de frases que aparecem no texto. str -> int"""
    a = txt.count('...')
    if a>0:
        b = txt.count('.') - (a*3)
    else:
        b  = txt.count('.')
    c = txt.count('!')
    d = txt.count('?')
    return a+b+c+d