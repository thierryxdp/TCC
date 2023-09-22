def par(x):
    """ função que retorna true se o o número 
    for par , e false se não for , neste caso 
    int/float-> bool"""
    return x%2 ==0
def filtra_pares(t):
    """ função que pega uma tupla com quatro
    valores inteiros e retorna uma nova tupla
    contendo os valores pares da tupla anterior.
    Assinatura: tup --> tup
    """
    pares =()
    if par(t[0]):
        pares = pares + t(t[0],)
        if par(t[1]):
            pares = pares + t(t[1],)
            if par(t[2]):
                pares = pares + t(t[2],)
                if par(t[3]):
                    pares = pares + t(t[3],)
                    return pares