def filtra_pares(a,b,c,d):
    """parametros de entrada:int; retorno:int"""
    tupla=(a,b,c,d)
    pares= ()
    for elemento in tupla:
        if elemento%2==0:
            pares=pares+(elemento,)
    return pares