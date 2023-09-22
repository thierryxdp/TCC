def buscaSetor(setor, dados):
    '''Dados uma matriz com os dados dos funcionários de uma empresa e um setor,
       retorna os dados dos funcionários que trabalham naquele setor;
       str, list -> list'''
    funcionarios_encontrados = []
    for funcionario in dados:
        if funcionario[2] == setor:
            list.append(funcionario, funcionarios_encontrados)
    for dados in funcionario_encontrados:
        del dados[2]
    return funcionarios_encontrados