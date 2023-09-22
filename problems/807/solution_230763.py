#a funcao retorna quantas frases tem o texto
#string->int
def conta_frases(texto):
    m = str.count(texto, '!')
    a = str.count(texto, '?')
    x = str.count(texto, '...')
    return m + a + x