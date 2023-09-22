def eh_quadrada(matriz):
    """Função que retorna True se  matriz é quadrada e False
    se não é quadrada
    Entrada: lista
    Saída: bool """
    linhas = len(matriz)    
    if linhas == 0 :
        return True   
    colunas = len(matriz[0])
    return linhas == colunas