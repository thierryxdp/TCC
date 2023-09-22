def busca(setor,matriz):
    '''Rcebe uma matriz 6x10 e o setor desejado e retorna os dados de todos 
    os funcionarios do setor informado;
    str,list->list'''
    
    lista_info=[]
    for i in matriz:
        if i[2]==setor:
            lista_info.append(i[0:2]+i[3:])
    return lista_info