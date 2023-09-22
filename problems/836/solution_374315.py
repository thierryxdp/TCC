def busca(setor,matriz):
    '''procura e retorna todos os funcionários e suas informações de um setor determinado
    	list,str->list'''
    
    lista=[]
    t=[]
    
    for i in range(len(matriz)):
        
        
        if setor in matriz[i]:
          
        
        	lista.append(matriz[i])
            t=lista[:]
            t.remove(lista[i][2])
    
    return t