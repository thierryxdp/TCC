def busca(setor, matriz):
    """
    Função, que dado um setor e uma matriz, faz uma busca pelo banco de dados dos funcionários 
    e retorna os dados do funcionário em questão.
    string, list -> list
    """
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        if setor in matriz[i]:
            return [matriz[i]]
        i = i + 1
        
    return []