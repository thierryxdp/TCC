def busca (setor,matriz):
    '''função que dado o nome de um setor e uma matriz, retor
    na os dados de todos os funcionarios daquele setor;
    str,list->list'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,[i[0],i[1],i[3]])
    return resp