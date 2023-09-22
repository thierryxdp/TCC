def filtra_pares(tupla):
    """parametros de entrada:int; retorno:int"""
    tupla=(a,b,c,d)
    pares=()
    for elemento in tupla:
        if elemento%2==0:
            pares= pares+(elemento,)
    return pares