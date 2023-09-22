def busca (nome_setor,matriz):
    '''Retorna uma matriz com os dados dos funcionários com base no setor. str,list(list)->list. '''
    lista=[]
    for elem in range(len(matriz)):
        if nome_setor in matriz[elem]:
            lista.append(matriz[elem])
    return lista