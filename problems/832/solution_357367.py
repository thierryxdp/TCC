def eh_quadrada (matriz):
    """funçao que recebe uma matriz no formato lista de listas  e retorna se e quadrada ou nao;
    entrada: list;
    saida: bool."""
    
    linhas= len(matriz)
    colunas = len(matriz[0])
    
    if linhas == colunas:
        return True
    else:
        return False