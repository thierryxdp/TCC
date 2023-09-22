def busca(nome, matriz):
    
    num=0
    conta
    lista=[]
    for num in range(len(matriz)):
        if nome in matriz[num]:
            lista.append(matriz[num])
            
    for conta in range(len(lista)):
        lista.pop(lista[0][2])
        
    return lista