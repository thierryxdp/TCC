def busca(setor,matriz):
    '''retorna as informações de todos os funcionários da empresa
    em um determinado setor;
    string,list->list'''
    i=0
    for linha in matriz:
    while i< len(matriz):
        if matriz[i][2]==setor:
            list.remove(matriz[i],setor)
        else:
            list.remove(matriz,matriz[i])
        i+=1
    return matriz