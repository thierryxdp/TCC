def busca(nome, matriz):
    
    num=0
    lista=[]
    
    for num in range(len(matriz)):
        if nome in matriz[num]:
            lista.append(matriz[num])
            
    for num in range(len(lista)):
        lista.pop(lista[num][2])
        
    return lista