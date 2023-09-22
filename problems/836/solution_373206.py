def infor_s(lista):
    '''função que dada uma lista retorna o índice 2 da lista que equivale ao setor em que o funcionário trabalha'''
    return lista[2]

def busca(setor,matriz):
    '''função que dado setor e matriz com as informações dos funcionários de uma empresa, retorna os empregados que atuam no ramo solicitado na entrada'''
    ls=[]
    for i in matriz:
        if infor_s(i)== setor:
            k=[i[0],i[1],i[3]]
            list.append(ls,k)
    return ls