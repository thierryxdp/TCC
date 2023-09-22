def conta_frases(texto):
    ''''''
    pontofinal = len(str.split(texto,'.'))
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    frases = pontofinal + exclamacao + interrogacao + reticencias
    return frases