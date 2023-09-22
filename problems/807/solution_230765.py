#a funcao retorna quantas frases tem o texto
#string->int
def conta_frases(texto):
    x = str.count(texto, '...')
    texto= str.replace(texto, '...', '')
    n = str.count(texto, '.')
    m = str.count(texto, '!')
    a = str.count(texto, '?')
    return x + n + m + a