def busca(setor,matriz):
    '''retorna as informações de todos os funcionários da empresa
    em um determinado setor;
    string,list->list'''
    for linha in matriz:
        list.remove(linha,setor)
    return matriz