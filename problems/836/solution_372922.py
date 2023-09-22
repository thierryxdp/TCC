def busca(setor,matriz):
    """retorna os dados de todos os funcionarios que trabalham no setor requisitado"""
    """str, list -> list"""
    
    dados = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = [matriz[i][0],matriz[i][1],matriz[i][3]]
            list.append(dados,funcionario)
    return dados