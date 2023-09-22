def busca(filtro, matriz):
    
    final = []
    
    for a in range(len(matriz)):
    	if filtro in matriz[a][2]:
  
            resultado= (matriz[a])
            list.remove(resultado,filtro)
            list.append(final,resultado)
            
    return final