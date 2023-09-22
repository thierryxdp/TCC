def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um balor booleano
    list -> bool
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    
    for linhas in matriz:
        for colunas in matriz:
            if linhas == colunas:
                return True
            elif linhas == 0:
                return True
            else: 
                return False