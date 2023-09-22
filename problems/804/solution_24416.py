def filtra_pares(tupla):
    """recebe uma tupla com 4 elementos e retorna uma tupla com só os elementos pares dentre esses.
    tuple->tuple"""
    resultado=()
    if (tupla[0]%2)==0:
        resultado=resultado + (tupla[0],)
    if (tupla[1]%2)==0:
        resultado= resultado+ (tupla[1],)
    if (tupla[2]%2)==0:
        resultado= resultado+ (tupla[2],)
    if (tupla[3]%2)==0:
        resultado= resultado+ (tupla[3],)
    return resultado