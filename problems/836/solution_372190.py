def busca(setor,dados_funcionarios):
    """Função que recebe uma matriz e faz uma busca por setor, retornando os dados de todos os funcionários daquele setor
    entrada: str, list
    saída: list"""
    lista=[]
    for i in range(len(dados_funcionarios)):
        if dados_funcionarios[i][2]==setor:
            lista=lista+[dados_funcionarios[i][0]]+[dados_funcionarios[i][1]]+[dados_funcionarios[i][3]]
    return [lista]