def conta_frases (texto):
    """recebe uma frase e retorna o numero de palavras nela contidas
    string -> int"""
    
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    final = str.count(texto, '.')
    
    total = exclamacao + interrogacao + reticencias + final
    
    if ('...' in texto and '.' in texto):
        return total - 3 
    
    else: 
        return total