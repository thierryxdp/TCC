def busca(setor, matriz):
    ''' retorna os dados de todos os funcionários da
    empresa do setor informado; entrada-> setor,matriz;
    str,list(mat)-> list(list)'''
    lista=[]
    for linha in matriz:
        if setor in linha:
            list.append(lista,linha)
            list.remove(lista,setor)
    return lista