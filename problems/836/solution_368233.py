def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                lista.append(matriz[i])
                if len(matriz)<2:
                    lista1=lista[0] 
                    return list.remove(lista1,setor)
                if len(matriz)==2:
                    lista1=lista[0]
                    lista2=lista[1]
                    del lista1[2]
                    del lista2[2]
                    return  [lista1,lista2] 
                else:
                    return lista