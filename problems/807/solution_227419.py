def conta_frases(frases):
    """Essa função retorna quantas frases existem em um texto informado
    string --> int"""
    
    import re
    frase_separada = str.re.split(frases,".|?|!|..."))
    return len(frase_separada)