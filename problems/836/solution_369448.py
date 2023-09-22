def busca(setor, registro):
    '''Função que recebe uma matriz com registro de dados dos
    funcionários de uma empresa e retorna apenas os dados referentes
    ao setor solicitado.
    str,str ->list'''
    informacao_solicitada = []
    for funcionario in registro:
        for setores in funcionario:
            if setor in setores:
            	list.append(informacao_solicitada, [funcionario[0], funcionario[1], funcionario[3]])
    
    return informacao_solicitada