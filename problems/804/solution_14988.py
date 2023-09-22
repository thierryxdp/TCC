def filtra_pares(tupla):
    tupla_retorno=()
    if tupla[0]%2==0:
        tupla_retorno= tupla_retorno + (tupla[0],)
    if tupla[1]%2==0:
        tupla_retorno= tupla_retorno + (tupla[1],)
    if tupla[2]%2==0:
        tupla_retorno=tupla_retorno + (tupla[2],)
    if tupla[3]%2==0:
        tupla_retorno= tupla_retorno + (tupla[3],)
    return tupla_retorno