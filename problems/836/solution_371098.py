def busca(n,matriz):
    '''função que dada uma matriz,faça uma busca no setor da empresa e retorna todos os dados de todos os funcionários:list,list->list'''
    cont = []
    for i in range(len(matriz)):
        if x == (matriz[i][2]):
            cont.append(matriz[i][:2] + [matriz[i][:-1]])
    return cont