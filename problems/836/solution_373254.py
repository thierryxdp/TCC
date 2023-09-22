def informacao_se(lista):
    '''Dado uma lista retorna o indice 2 da lista equivalente'''
    return lista[2]


def busca(setor,matriz):
    '''Dado o setor e a matriz com as informações dos funcionarios, retona todos os funcionais daquele setor'''
    ls=[]
    for i in matriz:
        if informacao_se(i)==setor:
            k=[i[0],i[1],i[3]]
            list.append(ls,k)
    return ls