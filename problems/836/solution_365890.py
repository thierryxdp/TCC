def busca(setor, matriz):
    """dada a matriz de funcionários de uma empresa, onde cada linha representa um funcionário e cada uma das quatro
    colunas representa, respectivamente, cada uma das seguintes informações: nome, registro, setor e telefone; a função
    recebe tal matriz e o nome de um setor da empresa e retorna os dados de todos os funcionários daquele setor; 
    str, list -> list"""
    setor = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            setor += [matriz[i]]
                
    return setor