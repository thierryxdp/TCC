def filtra_pares(p):
    """Função que filtra a tupla com 4 elesmentos e retorna os elementos pares na mesma ordem;
    tupla -> tupla"""
       tupla = ()
    if p[0]%2 == 0:
        tupla=tupla+(p[0],)
    if p[1]%2 == 0:
        tupla=tupla+(p[1],)
    if p[2]%2 == 0:
        tupla=tupla+(p[2],)
    if p[3]%2 == 0:
        tupla=tupla+(p[3],)
    return tupla