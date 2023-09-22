def busca(setor,matriz):
    ''' Dado uma matriz com os dados dos funcionarios de uma
    	empresa e o setor que se quer fazer a busca, retorna
        os dados de todos os funcionarios daquele setor
        str,list -> list
    '''
    acumulador = []
    contador = 0
    for i in range(len(matriz)):
        if setor.lower() in matriz[i][2].lower():
            acumulador.append(matriz[i])
            acumulador[contador].pop(2)
            contador += 1
    return acumulador