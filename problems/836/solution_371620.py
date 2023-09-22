def busca(setor,matriz):
    '''retorna as informações de todos os funcionários da empresa
    em um determinado setor;
    string,list->list'''
    i=0
    busca=[]
    for linha in matriz:
        if linha[2]==setor:
            del linha[2]
            list.append(busca,linha)
    return busca