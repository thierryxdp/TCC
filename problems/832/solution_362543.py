def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    
    for i in range(linhas):
       	for j in range(colunas):
            if matriz[i] == matriz[j]:
                return True
            else: 
                return False
    return False