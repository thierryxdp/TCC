def eh_quadrada(matriz):
    """Função que dada uma matriz indentifica se ela é uma matriz quadrada.
       list->bool
       
       Parâmetros:
       matriz: A matriz que será avaliada como quadrada ou não.
       
       returns: Caso a matriz seja quadrada retornará True, caso contrário 
                retornará False.
    """
    if len(matriz) == len(matriz[0]) or matriz == []:
        return True
    else:
        return False