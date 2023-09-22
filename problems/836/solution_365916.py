def busca(setor,matriz):
    '''Função que recebe um setor e uma matriz com os dados dos funcionários de uma empresa e retorna todos os dados de todos os funcionários daquele setor; str,list->list'''
    listasetor=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            nome= matriz[i][0]
            registro=matriz[i][1]
            telefone=matriz[i][3]
            list.append(listasetor,[nome,registro,telefone])
        else:
                listasetor=listasetor
    return listasetor