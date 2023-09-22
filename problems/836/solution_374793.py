def busca(dados, setor):
    """ Função que recebe uma matriz contendo os dados
    dos funcionários e um setor da empresa, realiza uma busca
    e retorna os dados de todos os funcionários daquele setor
    list -> list"""
    funcionarios_setor = []
    for i in dados:
        if i[2] == setor:
            funcionarios_setor.append(i[0:2] + i[3:])
    return funcionarios_setor