def busca(setor, matriz):
    '''
    função que recebe uma matriz determinando os dados de 
    funcionários de uma empresa e uma string de um setor
    da empresa. A função retorna os dados dos funcionários
    daquele setor
    '''
    funcionario = []
    for elem in matriz:
        if elem[2] == setor:
            funcionario.append(elem[:2] + elem[3:])
    return funcionario