def busca(setor, info_funcionarios):
    '''Funcao que, dado um setor e uma matriz com informacoes
    de funcionarios (info_funcionarios), realiza um busca e 
    retorna uma lista com os dados de todos os funcionarios
    que trabalham no setor em questao.
    Str, list -> List'''
    lin = len(info_funcionarios)
    lista = []
    
    for i in range(lin):
        if info_funcionarios[i][2] == setor:
            lista += [[info_funcionarios[i][0], info_funcionarios[i][1], info_funcionarios[i][3]],]
    return lista