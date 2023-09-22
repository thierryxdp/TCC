def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                lista.append(matriz[i])
                if len(lista)==0:
                    return lista
                if len(lista)==1:
                    lista1=lista[0]
                    del lista1[2]
                    return [lista1]
                if len(lista)==2:
                    lista1=lista[0]
                    del lista1[2]
                    lista2=lista[1]
                    del lista2[2]
                    return [lista1,lista2]