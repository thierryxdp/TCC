# Essa função retorna 
def conta_frases(texto):
    p0=texto.split(texto,"...")
    p1=texto.count('.')
    p2=texto.count('!')
    p3=texto.count('?')
    p4=texto.count('...')
    return p1+p2+p3+p4