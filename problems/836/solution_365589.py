def busca(funcao,matriz):
    
    
    lista = []
    
    for i in range(0,3):
        if funcao in matriz[i]:
            del matriz[i][2]
            list.append(lista,matriz[i])
        
    return lista