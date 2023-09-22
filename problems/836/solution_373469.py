def busca(setor, matriz):
    """
    Função, que dado um setor e uma matriz, faz uma busca pelo banco de dados dos funcionários 
    e retorna os dados do funcionário em questão.
    string, list -> list
    """
    
    linhas = len(matriz)
    if linhas == 0:
        return []
    else:
        colunas = len(matriz[0])