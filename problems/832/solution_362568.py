def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    linhas = len(matriz)
    
    
    for i in range(linhas):
        if linhas != None:
            colunas = len(matriz[0])
        else:
            return True
        for j in range(colunas):
            if linhas == colunas or linhas and colunas == 0:
                return True
            else: 
                return False