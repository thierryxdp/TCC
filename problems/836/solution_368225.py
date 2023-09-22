def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                lista.append(matriz[i])
            lista[0][2]=''
            lista[1][2]=''
          
    return  lista