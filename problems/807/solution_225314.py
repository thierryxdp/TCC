def conta_frases(frases):
    """Função que conta as frases de uma determinada string
       str->int"""
    A= str.partition(frases,.)
    B= str.partition(A,!)
    C= str.partition(B,?)
    D= str.partition(C,...)
    return len(D)