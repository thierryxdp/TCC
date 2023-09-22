def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                lista.append(matriz[i])
                lista1=lista[0]
                lista2=lista[1]
                list.remove(lista1,setor)
                list.remove(lista2,setor)
    return [lista1,lista2]