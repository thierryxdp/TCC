def busca(setor,matriz):
    '''
       função que recebe uma matriz fazendo uma 
       busca por setor, dado um nome de um setor da
       empresa, a função retorna os dados de todos os
       funcionarios daquele setor.
       
    '''
    ret=[]
    for i in matriz:
        if (i[2])==setor:
            ret.append(i[0:2]+i[3:])
    return ret