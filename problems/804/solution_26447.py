def filtra_pares(tuplas):
    """parametros de entrada:int; retorno:int"""
    pares=()
    for elemento in tupla:
        if elemento%2==0:
            pares= pares+(elemento,)
    return pares