def busca(setor,m):
    '''
    	essa função recebe uma matriz e um detrmionado setor, e, caso esse setor esteja presente na matriz, ela retorna os dados
        dos funcionários atuantes nesse setor específico; caso não, retorna uma lista vazia
        str,list->list
    '''
    linha = []
    nLinha = len(m)
    #o num de colunas sempre será o mesmo 4, ou seja, len(m[0]) = 4
    if setor in m:
        for i in range(nLinha):
            if setor in m[i]:
                list.append(linha, m[i])
                
    return linha