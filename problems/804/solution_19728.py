def filtra_pares(n):
     '''função que recebe um tupla de 4 elementos inteiros e devolve somente seus numeros pares; tuple->tuple'''
    tupla=()
    if n[0]%2==0:
        return tupla=tupla+(n[0],)
    if n[1]%2==0:
        return tupla=tupla+(n[1],)
    if n[2]%2==0:
        return tupla=tupla+(n[2],)
    if n[3]%2==0:
        return tupla=tupla+(n[3],)
    return tupla