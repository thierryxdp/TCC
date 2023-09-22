def busca(setor,matriz_funcionarios):
    '''teste'''
    
    funcionarios_setor=[]
    
    for i in range(len(matriz_funcionarios)):
        funcionarios= matriz_funcionarios[i]
        
        if setor in funcionarios:
            del matriz_funcionarios[i][2]
            funcionarios_setor+=[matriz_funcionarios[i]]
            
    return funcionarios_setor