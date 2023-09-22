def conta_frases(frases):
    """Essa função retorna quantas frases existem em um texto informado
    string --> int"""
    
    import re
    frase_separada = resplit(frases,".|?|!|..."))
    return len(frase_separada)