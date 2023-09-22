def busca(setor,matriz):
    '''dada uma matriz com dados de funcionários de uma empresa, retorna uma matriz com os dados de um determinado setor;
    str, list --> list'''
    lista=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(lista,[matriz[i][0],matriz[i][1],matriz[i][3]])
    return lista