def busca(setor,matriz):
    '''retorna as informações de todos os funcionários da empresa
    em um determinado setor;
    string,list->list'''
    for linha in matriz:
        if linha[2]==setor:
            list.remove(linha,setor)
        else:
            list.remove(matriz,linha)
    return matriz