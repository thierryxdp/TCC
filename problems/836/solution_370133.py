def busca(setor,matriz):
    '''Dada uma matriz com as informacoes de funcionarios
    de uma empresa e um setor, retorna os dados de todos 
    os funcionarios daquele setor
    list, str -> list'''
    
    lista_final=[]
    
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            lista=[matriz[i][0]+matriz[i][1]+matriz[i][3]]
            list.append(lista_final,lista)
    return lista_final