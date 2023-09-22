def busca(setor,m):
    '''
    	essa função recebe uma matriz contendo informações sobre os funcionários de uma empresa e um determinado setor a ser escolhido,
        e retorna os dados de cada funcionário presentes nesse setor específico; caso nenhum registro seja encontrado, retorna uma 
        lista vazia
        str,list->list
    '''
    linha = []
    nLinha = len(m)
    nColuna = len(m[0])
    for i in range(nLinha):
        for j in range(len(m[i])):
            if setor in m[i]:
                ma[i].remove(setor)
                list.append(linha,m[i]) 
    return linha