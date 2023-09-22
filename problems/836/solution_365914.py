def busca(setor,matriz):
    '''Função que recebe um setor e uma matriz com os dados dos funcionários de uma empresa e retorna todos os dados de todos os funcionários daquele setor; str,list->list'''
    listasetor=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            nome= matriz[i][j][0]
            registro=matriz[i][j][1]
            telefone=matriz[i][j][3]
            list.append(listasetor,list(nome,registro,telefone))
        else:
                listasetor=listasetor
    return listasetor