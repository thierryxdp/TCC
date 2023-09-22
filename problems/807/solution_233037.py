def conta_frases(txt):
    """da um texto e retorna a qntdd de frases nele, considerando "...", ".",
    "?" e "!" como intervalos entre frases
    
    str -> int
    """
    return txt.count("...") + txt.count("!") + txt.count("?") + txt.count(".")