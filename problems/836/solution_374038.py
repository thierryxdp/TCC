def busca (matriz):
    ''' '''
    funcionarios_encontrados = list()
    
    for funcionario in matriz:
        setor_func = funcionario[2]
        if setor == setor_func:
            
            func_sem_setor = funcionario[:]
            del func_sem_setor[2]
            
            funcionarios_encontrados.append(funcionario)
            
    return funcionarios_encontrados