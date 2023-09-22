def busca(setor,matriz):
    """Funcao que, dado um setor e uma matriz de entrada,
    no qual a matriz possui informacoes referentes ao nome,
    ao registro, ao setor e ao telefone de um funcionario,
    retorna os dados de todos os funcionarios daquele setor;
    str, list[list] -> list"""
    dados_setor=[]
    for linhas in matriz:
        if linhas[2]==setor:
            dados_setor+=[[linhas[0],linhas[1],linhas[3]]]
    return dados_setor