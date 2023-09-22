def busca(setor, matriz):
    """
    Função, que dado um setor e uma matriz, faz uma busca pelo banco de dados dos funcionários 
    e retorna os dados do funcionário em questão.
    string, list -> list
    """
    
    
    for i in range(len(matriz)):
            if setor in matriz:
                list.remove(matriz,setor)
                return matriz
            else:
                return []