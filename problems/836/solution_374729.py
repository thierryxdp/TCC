def busca(setor,matriz):
    '''função que retorna os dados de todos os funcionários de um setor, dado o setor e a matriz que contém todos os funcionários da empresa;str,list->list'''
    funcionarios=[]
    for linha in matriz:
        if linha[2]==setor:
            list.append(funcionarios,[linha[0],linha[1],linha[3]])
    return funcionarios