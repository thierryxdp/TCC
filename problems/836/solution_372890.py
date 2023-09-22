def busca(setor,matriz):
    '''funcao que dada uma matriz contendo dados de funcionarios armazenados e dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor;
       str, list(list)-> list'''
    listafinal=[]
    for linha in range(len(matriz)):
        for coluna in matriz[linha]:
            if coluna== setor:
                list.append(listafinal, matriz[linha])
                listafinal= list.remove(listafinal,setor)
    return listafinal