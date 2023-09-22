def busca(setor, matriz):
    ''' Dada uma matriz contendo:
    	[nome, registro, setor, telefone]
	
    busque o funcionário pelo setor.
    
    list(list) --> list'''
    
    funcionarios_encontrados = list()
    
    for funcionario in matriz:
        
        # setor do funcionário
        setor_func = funcionario[2]
        
        if setor == setor_func:
            # encontrei um funcionario do setor buscado
            funcionarios_encontrados.append(funcionario)
	
    return funcionarios_encontrados