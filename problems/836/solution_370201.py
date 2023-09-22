def busca(setor,matriz):
    ''' Dado uma matriz com os dados dos funcionarios de uma
    	empresa e o setor que se quer fazer a busca, retorna
        os dados de todos os funcionarios daquele setor
        str,list -> list
    '''
    acumulador = []
    for i in range(len(matriz)):
        if nome.lower() in matriz[i][0].lower():
            acumulador.append(matriz[i])
    return acumulador