def filtra_pares(elem):
    tupla_retornar=()
    if (elem[0]%2==0):
        tupla_retornar=(elem[0],)
    if elem[1]%2==0:
        tupla_retornar=tupla_retornar+(elem[1],)
    if elem[2]%2==0:
        tupla_retornar=tupla_retornar+(elem[2],)
    if elem[3]%2==0:
        tupla_retornar=tupla_retornar+(elem[3],)
    return tupla_retornar