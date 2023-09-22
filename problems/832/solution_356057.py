def eh_quadrada(matriz):
    '''
    Verifica se certa matriz é quadrada - ou seja, se possui o mesmo número de
    linhas e colunas - ou não. Obs: Considera-se uma matriz vazia (sem nenhuma
    linha nem coluna) como quadrada.
    list -> bool

    Parameters:
    matriz: Parâmetro do tipo lista (list).

    Returns:
    Um valor booleano:
      # True: caso a matriz informada seja quadrada;
      # False: caso contrário.      
    '''

    matriz = [list()]
    qtde_linhas = len(matriz)
    if qtde_linhas == 1:
        qtde_colunas = len(matriz[0])

    if qtde_linhas == qtde_colunas or (qtde_linhas == 1 and qtde_colunas == 0):
        return True
    else:
        return False