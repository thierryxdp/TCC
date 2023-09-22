def busca(setor,m):
    '''recebe o nome o setor e uma matriz em que cada linha contém
    os dados de um funcionário: nome, registro, setor e telefone.
    a função retorna uma lista contendo todos os funcionários
    presente no setor de entrada.
    str, list(list)->list(list)'''
    funci = []
    copia = []
    for i in range(len(m)):
        if m[i][2] == setor:
            copia = m[i][:]
            list.remove(copia,m[i][2])
            list.append(funci,copia)
            
    return funci