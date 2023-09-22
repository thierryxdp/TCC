def busca(setor,m):
    """recebe uma string representando o setor e uma matriz com os dados dos funcionários e retorna uma outra contendo os dados dos funcionários daquele setor;str,list->list"""
    dados=[]
    for i in range(3):
            if setor in m[i]:
                dados=dados+m[i][0:2]+m[i][3]
    return dados