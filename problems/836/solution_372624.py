def busca(string,dados):
    '''
    Função que realiza uma busca por setor em uma certa matriz de dados, e depois retorna os dados dos funcionários daquele setor.
    str,list -> list
    '''
    funcionarios = []
    for elem in range(0,len(dados)):
        if string in dados[elem]:
            funcionarios = funcionarios + [dados[elem]]
            dados[elem].remove(string)
    return funcionarios