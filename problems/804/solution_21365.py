def filtra_pares(tup):
    """Função que recebe quatro números dentro de uma tupla e retorna uma tupla contendo apenas os pares.
assinatura: tuple -> tuple
"""
    ntp=()
    if tup[0]%2==0:
        ntp=ntp+('tup[0]',)
    if tup[1]%2==0:
        ntp=ntp+('tup[1]',)
    if tup[2]%2==0:
        ntp=ntp+('tup[2]',)
    if tup[3]%2==0:
        ntp=ntp+('tup[3]',)
        return ntp