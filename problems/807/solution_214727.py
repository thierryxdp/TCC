def conta_frases (texto) :
    """Funcao que retorne o numero de frases que aparecem no texto"""
    a = str.count(texto, '!')
    b = str.count(texto, '?')
    c = str.count(texto, '.')
    d = str.count(texto, '...')
    texto = (a+b+c+d)-(3*d)
    return texto