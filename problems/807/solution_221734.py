def conta_frases(texto):
    ''''''
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    pontofinal = str.count(texto,'.') - 3*reticencias
    
    frases = pontofinal + exclamacao + interrogacao + reticencias
    return frases