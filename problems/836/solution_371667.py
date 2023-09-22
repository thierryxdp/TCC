def busca(setor, matriz):
    '''função que, dada uma matriz com os dados dos
    funcionários, realiza uma busca por setor, ou seja, 
    dado um nome de um seto da empresa, a função retorna os 
    dados de todos os funcionários daquele setor.
    str,list(list)->list(list)'''
    registro = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            matriz[i].remove(setor)
            registro = registro + [matriz[i]]
    return registro