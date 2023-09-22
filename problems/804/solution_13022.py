def filtra_pares(tuplaOriginal):
    """ Dado uma tupla com 4 números inteiros, a função retorna
    uma nova tupla contendo apenas os elementos pares da tupla
    original.
    Parametros de Entrada: tupla
    Retorna: tupla"""
    tuplaAuxiliar=()
    if (tuplaOriginal[0]%2)==0:
        tuplaAuxiliar= tuplaAuxiliar+(tuplaOriginal[0],)
    if (tuplaOriginal[1]%2)==0:
        tuplaAuxiliar= tuplaAuxiliar+(tuplaOriginal[1],)
    if (tuplaOriginal[2]%2)==0:
        tuplaAuxiliar= tuplaAuxiliar+(tuplaOriginal[2],)
    if(tuplaOriginal[3]%2)==0:
        tuplaAuxiliar= tuplaAuxiliar+(tuplaOriginal[3],)
    return tuplaAuxiliar