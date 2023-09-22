def busca(setor,matriz):
    ''' Dado uma matriz com os dados dos funcionarios de uma
    	empresa e o setor que se quer fazer a busca, retorna
        os dados de todos os funcionarios daquele setor
        str,list -> list
    '''
    acumulador = []
    for i in range(len(matriz)):
        #for j in range(len(matriz[0])):
        if setor.lower() in matriz[i][2].lower():
            acumulador.append(matriz[i])
            acumulador[0].pop(2)
    return acumulador