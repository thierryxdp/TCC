def busca(setor, matriz):
    ''' retorna os dados de todos os funcionários da
    empresa do setor informado; entrada-> setor,matriz;
    str,list(mat)-> list(list)'''
    lista=[]
    for linha in matriz:
        if setor in linha:
            list.append(lista,linha[1])
    	else:
            lista=[]
            
    return lista