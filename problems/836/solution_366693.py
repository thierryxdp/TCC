def busca(setor,matriz):
    '''funcao que quando feita a busca por um setor, retorna os dados te todos
    os funcionarios daquele setor, tuple->list'''
    lista=[]
    for i in range(len(matriz)):
        if setor ==matriz[i][2]:
            list.remove(matriz[i],setor)
            lista=lista+[matriz[i]]
    return lista