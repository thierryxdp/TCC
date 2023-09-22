def conta_frases(texto):
    """Retorna o número de frases de um texto dado; str -> int"""
    y = int(str.count(texto,".")) 
    x = int(str.count(texto,"..."))/3
    z = int(str.count(texto,"!"))
    w = int(str.count(texto,"?"))
    return x+y+z+w