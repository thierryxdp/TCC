def conta_frases (texto):
    """recebe uma frase e retorna o numero de palavras nela contidas
    string -> int"""
    
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    final = str.count(texto, '.')
    
    
    return exclamacao + interrogacao + (reticencias - 3) final