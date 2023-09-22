def eh_quadrada(matriz: list) -> bool:
    """Identifica se uma matriz é quadrada ou não

       Parameters:
       matriz: Matriz formada por listas a ser analisada, na qual as listas
       dentro da matriz são as linhas e as listas dentro das listas são as
       colunas

       Return:
       Dado o parâmetro "matriz", identifica se uma matriz é quadrada ou não, e,
       caso seja, retorna True, caso contrário, retorna False

       Examples:
       eh_quadrada([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == True
       eh_quadrada([[1, 1], [1, 1], [1, 1]]) == False
       eh_quadrada([]) == True
    """

    if matriz == []:
        return True

    else:
        return len(matriz) == len(matriz[0])