def filtra_pares(elem1,elem2,elem3,elem4):
    tupla_retornar=()
    if elem1%2==0:
        tupla_retornar=tupla_retornar+(elem1,)
    if elem2%2==0:
        tupla_retornar=tupla_retornar+(elem2,)
    if elem3%2==0:
        tupla_retornar=tupla_retornar+(elem3,)
    if elem4%2==0:
        tupla_retornar=tupla_retornar+(elem4,)
    return tupla_retornar