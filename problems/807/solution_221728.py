def conta_frases(texto):
    ''''''
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    if '...' in texto:
        pontofinal = str.count(str.strip(texto,'...'),'.')
        
    else:
        pontofinal = str.count(texto,'.')

    frases = pontofinal + exclamacao + interrogacao + reticencias
    return frases