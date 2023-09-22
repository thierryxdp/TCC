def eh_quadrada(A):
    """Função que identifica se uma matriz e quadrada verificando seu numero de linhas e colunas.
    Parametros: list->bool"""
    if A == []:
        return True
    for linha in range(len(A)):
        for coluna in range(len(A[linha])):
            if len(A) == len(A[0]):
                return True
        else:
            return False