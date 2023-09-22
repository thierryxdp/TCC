def busca(setor,matriz):
    '''procura e retorna todos os funcionários e suas informações de um setor determinado
    	list,str->list'''
    
    lista=[]
    t=[]
    
    for i in range(len(matriz)):
        
        
        if setor in matriz[i]:
            
            t.append(matriz[i])
            del t[2]
            
            
        lista.append(t)
            
    
    return lista