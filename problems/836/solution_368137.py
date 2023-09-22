def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                lista.append(matriz[i])
                lista1=list.remove(lista,setor)                      
        
    return  lista