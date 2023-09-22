conta_frases(texto):
    """Funcao que dado um texto armazenado em uma string,
    conta o numero de frases que aparecem.
    str -> int"""
    
    exclamacao = texto.count("!")
    interrogacao = texto.count("?")
    ponto = texto.count(".")
    reticencias = texto.count("...")
    total = exclamacao + interrogacao + ponto + reticencias
    
    if reticencias == 0:
        return total
    else:
        return total - reticencias*3