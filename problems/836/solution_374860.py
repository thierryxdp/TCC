def busca(setor, matriz):
    
    
    lista = []
    for e in range(len(matriz)):
    	if setor in matriz[e][2]:
            result = (matriz[e])
            list.remove(result,setor)
            list.append(lista,result)
            
    return lista