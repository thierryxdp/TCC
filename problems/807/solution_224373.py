def conta_frases(texto):
    #Conta o número de frases que aparecem no texto
    b = texto.split('...')
    c = ",".join(b)
    d = c.split('.')
    e = ",".join(d)
    f = e.split('?')
    g = ",".join(f)
    h = g.split('!')
    return len(h)