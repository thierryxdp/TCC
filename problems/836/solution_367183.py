def busca(setor,m):
    """recebe uma string representando o setor e uma matriz com os dados dos funcionários e retorna uma outra contendo os dados dos funcionários daquele setor;str,list->list"""
    dados=[]
    for i in range(3):
            if setor==m[i][2]:
                dados=dados+[m[i]]
                list.remove(dados[i],setor)
                return dados
            else:
                return []