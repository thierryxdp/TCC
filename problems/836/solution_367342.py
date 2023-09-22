def busca(setor,matriz):
    """
    Função que recebe uma matriz com os dados referentes aos funcionários
    de uma empresa e um setor e retorna uma matriz com os dados de todos
    os funcionários que trabalham nesse setor.
    
    str, list --> list
    """
    lista=[]
    
    for i in matriz:
        if i[2]==setor:
            lista.append(i)
    return lista