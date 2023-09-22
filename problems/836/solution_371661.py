def busca(setor,dados):
    '''Dado o setor e os dados dos 
    funcionarios da empresa,a função retorna
    todos os dados impostos lista de acordo com
    o setor pesquisado. lista,tupla->Tupla'''
    lista1=[]
    for i in range(len(dados)):
        if setor in dados[i]:
            resulta=[dados[i][0],dados[i][1],dados[i][3]]
            list.append(lista1,resulta)       
    return lista1