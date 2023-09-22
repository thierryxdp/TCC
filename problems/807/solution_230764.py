#a funcao retorna quantas frases tem o texto
#string->int
def conta_frases(texto):
    n = str.count(texto, '.')
    m = str.count(texto, '!')
    a = str.count(texto, '?')
    x = str.count(texto, '...')
    return n + m + a + x