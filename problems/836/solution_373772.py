def busca(setor,matriz):
    '''funcao que dada uma matriz contendo dados de funcionarios armazenados e dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor;
       str, list(list)-> list'''
    listafinal=[]
    i=0
    for linha in range(len(matriz)):
        for coluna in matriz[linha]:
            if coluna == setor:
                list.append(listafinal, matriz[linha])
                list.remove(listafinal[i], setor)
                i=i+1
    return listafinal