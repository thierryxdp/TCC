def conta_frases(texto):
    ''''''
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    if '...' not in texto:
        pontofinal = str.count(texto,'.')
    else:
        pontofinal = str.count(str.strip(texto,'...'),'.')
        frases = pontofinal + exclamacao + interrogacao + reticencias
    return frases