def busca(setor,matriz):
    '''
    	Funcao recebe uma string contendo um setor da empresa
        e uma matriz com os dados dos funcionarios, e retorna
        uma lista de listas com os dados de todos os 
        funcionarios do setor informado.
        str, list -> list
        
    '''
    dados = []
    for i in range(len(matriz)):
        funcionario = []
        if setor == matriz[i][2]:
            list.append(funcionario,matriz[i][0])
            list.append(funcionario,matriz[i][1])
            list.append(funcionario,matriz[i][3])
            list.append(dados, funcionario)
    return dados