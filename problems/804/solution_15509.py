def filtra_pares(s):
    """ Função que retorna os elementos pares da tupla
    tup -> tup """
    tupla_final=()
    if s[0]%2==0:
        tupla_final=tupla_final+(s[0],)
    if s[1]%2==0:
        tupla_final=tupla_final+(s[1],)
    if s[2]%2==0:
        tupla_final=tupla_final+(s[2],)
    if s[3]%2==0:
        tupla_final=tupla_final+(s[3],)
    return tupla_final