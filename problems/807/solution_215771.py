def conta_frases(texto):
    """Retorna o número de frases de um texto dado; str -> int"""
    y = int(str.count(texto,".")) 
    z = int(str.count(texto,"!"))
    w = int(str.count(texto,"?"))
    return y+z+w