def busca(setor,Matriz):
    '''
    '''
    departamento=[]
    for x in range(len(Matriz)):
        if setor in Matriz[x]:
            departamento=departamento+[Matriz[x]]
          
    for y in range(len(departamento)):
    	if setor in departamento[y]:
            list.remove(departamento[y],setor) 
            
    return departamento