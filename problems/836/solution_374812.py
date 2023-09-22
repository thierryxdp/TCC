def busca(setor, matriz):
    '''
    	Funcao que dada uma matriz, cuja as informacoes sejam nome, 
        registro, setor e o telefone de um funcionario, e um setor
        retorne os dados de todos os funcionarios daquele setor.
        str, list -> list
    '''
    resultado = []
    for i in range(len(matriz)):
        if setor in matriz[i][3]:
            list.append(resultado, matriz[i])
    return resultado