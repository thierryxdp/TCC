def eh_quadrada(matriz):
    """Função que dada uma matriz determina se ela é ou não quadrada
       
       parameters:
       matriz: Matriz que será avaliada pela função
       
       Returns:
       Retorna True caso a matriz seja quadrada e False se ela não for
       list -> bool"""
    linhas=len(matriz)
    colunas=len(matriz[0])
    if linhas == colunas:
        return True
    elif linhas == 0:
        return True
    else:
        return False