def filtra_pares(valores):
    """calculo e retorno de uma tupla contendo apenas os elementos pares"""
    pares=()
    if valores[0]% 2==0:
        pares+=(valores[0],)
    if valores[1]% 2==0:
        pares+=(valores[1],)
    if valores[2]% 2==0:
        pares+=(valores[2],)
    if valores[3]% 2==0:
        pares+=(valores[3],)
    return pares