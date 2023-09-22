def busca(setor,matriz_funcionarios):
    '''Função que realiza a busca dos funcionários que trabalham
em determiado setor de uma empresa. Dado o setor e uma matriz (matriz_funcionarios) 
representando a lista de funcionários dessa empresa e seus respectivos dados.
str,list[str]->list[str]'''
   
    funcionarios_setor=[]
    
    for i in range(len(matriz_funcionarios)):
        funcionarios= matriz_funcionarios[i]
        
        if setor in funcionarios:
            del matriz_funcionarios[i][2]
            funcionarios_setor+=[matriz_funcionarios[i]]
            
    return funcionarios_setor