#a funcao retorna quantas frases tem o texto
#string->int
def conta_frases(texto):
    return str.count(texto, '.', '!', '?', '...')