def busca(nome, matriz):
    
    num=0
    conta=0
    lista=[]
    for num in range(len(matriz)):
        if nome in matriz[num]:
            lista.append(matriz[num])
            
    #for conta in range(len(lista)):
    lista.remove(lista[0][2])
        
    return lista