def busca(setor,matriz):
    ''' apos informar um setor numa empresa e uma matriz contendo os dados de funcionarios, ira retorna uma lista de funcionarios daqeule setor
str, matris = list '''
    funcionarios = []
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i,j)
                list.append(funcionarios, i)
    return funcionarios