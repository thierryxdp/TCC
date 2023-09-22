def conta_frases(texto):
    """Retorna a quantidade de frases em determinado texto. str-> int"""
 
    a = str.count(texto, '.')
    b = str.count(texto, '!')
    c = str.count(texto, '?')
    d = str.count(texto, '...')
    if '...' in texto:
        a = a -1*(3*c)
    else:
        a = a
    
    return a+b+c+d