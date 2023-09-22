def busca(setor, matriz):
    ''' comando que dado um setor e uma matriz, retorna uma lista com as informações completas
    que encontram-se na matriz, daquele funcionario correspondente
    str,matiz --> list
    '''
    dados =[]
    
    for i in range(len(matriz)):
        funcionario = matriz[i]
        
        if setor in funcionario:
            nome = funcionario[0]
            registro =	funcionario[1]
            telefone =	funcionario[2]
            
            resultado = [nome,registro,telefone]
            dados.append[resultado]
	
    return dados