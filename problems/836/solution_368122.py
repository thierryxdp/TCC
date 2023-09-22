def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
         if setor in matriz[i]:
                nmatriz = matriz[i].remove(setor)
    return lista.append(nmatriz)