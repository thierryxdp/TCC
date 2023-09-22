def busca(setor, matriz):
    ''' Dada uma matriz contendo:
    	[nome, registro, setor, telefone]
	
    busque o funcionário pelo setor.
    
    list(list) --> list'''
    
    funcionarios_encontrados = list()
    
    for funcionario in matriz:
        
        # setor do funcionário
        setor_func = funcionario[2]
        
        # se encontrei um funcionario do setor buscado
        if setor == setor_func:
            # copio as informacoes do funcionario
            func_sem_setor = funcionario[:]
            
            # removo o setor do funcionario
            del func_sem_setor[2]
            
            # incluo na lista de encontrados
            funcionarios_encontrados.append(func_sem_setor)
	
    return funcionarios_encontrados