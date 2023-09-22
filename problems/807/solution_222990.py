def conta_frases (texto):
    """recebe uma frase e retorna o numero de palavras nela contidas
    string -> int"""
    
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    
    reticencias = str.count(texto, '...') - 3
    if (reticencias < 0):
        reticencias = 0
    	
    final = str.count(texto, '.')
    
    
    return exclamacao + interrogacao + reticencias + final