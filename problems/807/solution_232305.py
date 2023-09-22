def conta_frases(texto):
    """retorna a quantidade de frases em um texto, str---> int"""
    x=texto.count('.')
    y=texto.count('!')
    z=texto.count('?')
    a=texto.count('...')
    soma= x+y+z+a
    if '.' and '...' in texto:
        return soma-3*x
    else:
        return soma