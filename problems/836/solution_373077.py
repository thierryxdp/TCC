def busca(setor,m):
    '''recebe o nome o setor e uma matriz em que cada linha contém
    os dados de um funcionário: nome, registro, setor e telefone.
    a função retorna uma lista contendo todos os funcionários
    presente no setor de entrada.
    str, list(list)->list(list)'''
    funci = []
    for i in range(len(m)):
        if m[i][2] == setor:
            list.append(funci,m[i])
            list.remove(funci,m[i][2])
    return funci