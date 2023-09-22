def conta_frases( x ):
    """Função que calcula a quantidade de frases em um texto x
    string -> int"""
    a = str.count (x,'.')
    b = str.count (x,'?')
    c = str.count (x,'!')
    d = str.count (x ,'...')
    y = a+b+c+d
    return y - 3*d