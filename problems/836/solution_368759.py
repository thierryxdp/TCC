def busca(setor,matriz):
    '''Recebe uma matriz como a do exemplo e busca a ficha de 
    funcionarios por setor e retorna os dados de todos os 
    funcionarios daquele setor;
    str, list -> list'''
    lista=[]
    i=0
    for m in matriz:
        if setor in m:
            list.append(lista,[matriz[i]])
            list.remove(lista,matriz[i][2])
        i=i+1
    return lista