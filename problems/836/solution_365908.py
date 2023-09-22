def busca(setor,matriz):
    """Funcao que recebe ima matriz com dados de funcionarios e faz uma busca por setor retornando os funcuonarios que trabalham naquele setor;
    str,list->list"""
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            lista=lista+matriz[i]
    return lista