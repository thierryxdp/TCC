def busca(setor, dados):
    '''Retorna uma lista com os dados de
    todos os funcionarios do setor dado
    str, list --> list'''
    funcionarios = []
    for i in range(len(dados)):
        for j in dados[i]:
            if [dados[i][0],dados[i][1],dados[i][3]] not in funcionarios:
                if setor == dados[i][2]:
                    list.append(funcionarios, [dados[i][0],dados[i][1],dados[i][3]])
    return funcionarios