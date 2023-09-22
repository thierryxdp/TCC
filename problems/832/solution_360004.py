def eh_quadrada(A):
    """Função que identifica se uma matriz e quadrada verificando seu numero de linhas e colunas.
    Parametros: list->bool"""
    for linha in range(len(A)):
        for coluna in range(len(A[linha])):
            if linha == coluna and []:
                return True
        else:
            return False