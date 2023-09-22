def filtra_pares(tupla):
    """Apaga os números impares de uma tupla.
    tuple->tuple
    
    Parameters:
    tupla: A tupla que sera modificada.
    
    Returns:
    Uma nova tupla contendo apenas os números pares da tupla original.
    """
    x=()
    if int(tupla[0])%2==0:
        x=x+(tupla[0],)
    if int(tupla[1])%2==0:
        x=x+(tupla[1],)
    if int(tupla[2])%2==0:
        x=x+(tupla[2],)
    if int(tupla[3])%2==0:
        x=x+(tupla[3],)
    return x