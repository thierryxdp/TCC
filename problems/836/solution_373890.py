def busca(setor,matriz):
    '''Função que receba uma string e uma matriz e faz uma busca por setor e retorna uma lista com os dados de todos os funcionários daquele setor
    string,list->list'''
    C=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(C,matriz[i])
            del matriz[i][2]
    return C