def busca(setor,matriz):
    '''Funcao que receba um setor e uma matriz, fazendo a busca
       pelo setor, ou seja, dado um nome de um setor da empresa,
       a função retorna os dados de todos os funcionários daquele
       setor, no entanto, sem o setor dentro dessa lista.
       : param setor: str
       : param matriz: list
       : return: list 
    '''
    lista_1=[]
    lista=[]
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if setor==matriz[i][j]:
                 lista.append(matriz[i])
    for i in range(0,len(lista)):
        linha=[]
        for j in range(ncol):
            if lista[i][j]!=setor:
                linha.append(lista[i][j])
        lista_1.append(linha)
    return lista_1