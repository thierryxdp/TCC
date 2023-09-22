def busca(setor, matriz):
    ''' Esta função retorna os dados de todos os funcionários 
    de um determinado setor
    str,matiz -> list'''
    dados =[]
    
    for i in range(len(matriz)):
        funcionario = matriz[i]
        
        if setor in funcionario:
            nome = funcionario[0]
            registro =	funcionario[1]
            telefone =	funcionario[3]
            
            resultado = [nome,registro,telefone]
            dados.append(resultado)
	
    return dados