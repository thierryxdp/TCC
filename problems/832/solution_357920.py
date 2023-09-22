def eh_quadrada(M):
    """Recebe uma matriz M e verifica se o número de linhas dessa
       matriz é igual ao número de colunas
       Parâmetro de entrada:list(list)
       parâmetro de saída:bool"""
    if (len(M)==len(M[0])):
        return True
    elif (M=[]):
        return True
    else:
        return False