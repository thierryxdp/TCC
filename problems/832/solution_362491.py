def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    if linhas == 0 and colunas == 0:
        return True
    
    for i in matriz:
        for j in matriz:
            if linhas == colunas:
                return True
            else: 
                return False