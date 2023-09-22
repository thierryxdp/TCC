def filtra_pares(tupla):
    """Função que recebe uma tupla com 4 elementos e retorna uma tupla
contendo somente os parâmetros que forem par
assinatura: tuple --> tuple
testes:
filtra_pares() == 
filtra_pares() ==
"""
    t = ()
    if tupla[0]%2 == 0:
        t = t + (tupla[0],)
    if tupla[1]%2 == 0:
        t = t + (tupla[1],)
    if tupla[2]%2 == 0:
        t = t + (tupla[2],)
    if tupla[3]%2 == 0:
        t = t + (tupla[3],)
    return t