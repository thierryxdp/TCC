def conta_frases( x ):
    """Função que calcula a quantidade de frases em um texto x
    string -> int"""
    a = str.count (x,'.')
    b = str.count (x,'?')
    c = str.count (x,'!')
    d = str.count (x ,'...')
    z = a+b+c+d
    return z - 3*d