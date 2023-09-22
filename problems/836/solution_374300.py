def busca(matriz,setor):
    '''procura e retorna todos os funcionários e suas informações de um setor determinado
    	list,str->list'''
    
    lista=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
        
        	if setor == matriz[i][j]:
            
            	lista.append(matriz[i])
    
    return lista