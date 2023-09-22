def busca(setor,matriz):
    """ Função que recebe uma busca com os dados de 
        funcionários de uma empresa e faz uma busca 
        por setor, ou seja, dado um nome de um setor
        da empresa, a função retorna os dados de todos
        os funcionários daquele setor;
        string, list(list) -> list(list)"""
    dados_funcionarios = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                matriz[i] = matriz[i][0:2] + matriz[i][-1:]
                dados_funcionarios = dados_funcionarios + matriz[i]
    return dados_funcionarios