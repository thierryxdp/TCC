def busca(setor,matriz):
    '''retorna as informações de todos os funcionários da empresa
    em um determinado setor;
    string,list->list'''
    i=0
    while i< len(matriz):
        if linha[i][2]==setor:
            list.remove(linha,setor)
        else:
            list.remove(matriz,linha)
        i+=1
    return matriz