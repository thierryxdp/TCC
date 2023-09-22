def filtra_pares(n):
    """filtra os numeros pares de uma string,
    string -> string"""
    tupla=()
    if int(n[0])%2==0:
        tupla=tupla+(n[0],)
    if int(n[1])%2==0:
        tupla=tupla+(n[1],)
    if int(n[2])%2==0:
        tupla=tupla+(n[2],)
    if int(n[3])%2==0:
        tupla=tupla+(n[3],)
        return tupla
    else:
        return tupla