def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> list"""
    if '.' in texto:
        a = 2
    if '.' not in texto:
        a = 0
    if '!' in texto:
        b = 2
    if '!' not in texto:
        b = 0
    if '?' in texto:
        c = 2
    if '?' not in texto:
        c = 0
    if '...' in texto:
        d = 2
    if '...' not in texto:
        d = 0
        
        return a+b+c+d