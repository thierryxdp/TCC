def eh_quadrada(m):
    """Recebe uma matriz e retorna se a matriz é quadrada ou não.
Testes: eh_quadrada([[]]) == True
eh_quadrada([[1,2,7], [1,3,4]]) == False
Assinatura: mat --> bool
"""
    lin = len(m)
    col = len(m[0])
    if m == []:
        return True
    return lin == col