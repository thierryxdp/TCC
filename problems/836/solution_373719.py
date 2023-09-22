def busca(setor, dados):
    '''Dados uma matriz com os dados dos funcionários de uma empresa e um setor,
       retorna os dados dos funcionários que trabalham naquele setor;
       str, list -> list'''
    funcionarios_encontrados = []
    for funcionario in dados:
        if funcionario[2] == setor:
            funcionarios_encontrados.append(funcionario)
    for dados in funcionarios_encontrados:
        del dados[2]
    return funcionarios_encontrados