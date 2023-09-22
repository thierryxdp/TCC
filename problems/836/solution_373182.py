def busca(setor,m):
    '''
    	essa função recebe uma matriz e um determinado setor e retorna os dados
        dos funcionários desse setor, caso não tenha, retorna uma lista vazia
        str, list-> list
    '''
    nLinha = len(m)
    nColuna = len(m[0])
    nColuna = 4
    lista = []
    for i in range(nLinha):
        for j in range(nColuna):
            if (m[2] == setor):
                list.append(lista, (m[j][0],m[j][1],m[j][3]))
            else:
                lista = []
    return lista