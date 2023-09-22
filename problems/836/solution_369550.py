def busca(setor,matriz):
    '''
    Funcao que tem como entrada uma string indincando um setor
    e uma matriz com os dados de funcionarios de uma empresa.
    A funcao tem como retorno a os dados dos funcionarios de
    acordo com o setor dado como entrada.
    	Parametros:
        	entrada:
            	setor,matriz : str,list
            saida:
            	list
    '''
    lista = []
    a = len(matriz)
    for i in range(a):
        for j in matriz[i]:
            if j == setor:
                lista.append(matriz[i])
                del lista[i-1][2]
    return lista