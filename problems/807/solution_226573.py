def conta_frases(texto:str)->int:
    """conta o numero de frases em um texto"""
    n_texto=texto.split()
    n1=n_texto.count('.')
    n2=n_texto.count('...')
    n3=n_texto.count('!')
    n4=n_texto.count('?')
    n5=texto.count(',')
    return n1+n2+n3+n4+n5