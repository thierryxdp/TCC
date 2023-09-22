def busca(setor,Matriz):
    '''
    Função que recebe uma matriz com os dados de todos os funcionários e seleciona 
    os dados daqueles que pertencem ao setor dado como entrada. 
    str,list->list
    '''
    departamento=[]
    for x in range(len(Matriz)):
        if setor in Matriz[x]:
            departamento=departamento+[Matriz[x]]
          
    for y in range(len(departamento)):
    	if setor in departamento[y]:
            list.remove(departamento[y],setor) 
            
    return departamento