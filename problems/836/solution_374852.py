def busca(setor, matriz):
    '''
    	Funcao que dada uma matriz, cuja as informacoes sejam nome, 
        registro, setor e o telefone de um funcionario, e um setor
        retorne os dados de todos os funcionarios daquele setor.
        str, list -> list
    '''
    resultado = []
    for i in matriz:
        if setor in i[2]:
            list.append(resultado, i)
            del resultado[-1][2]
    return resultado