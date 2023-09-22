def busca(setor, matriz):
    ''' retorna os dados de todos os funcionários da
    empresa do setor informado; entrada-> setor,matriz;
    str,list(mat)-> list(list)'''
    lista=[]
    for linha in matriz:
        if setor in linha:
            list.append(lista,linha)
            if len(lista)==1:
    			list.remove(lista[0],setor)
            elif len(lista)==2:
                list.remove(lista[0],setor)
                list.remove(lista[1],setor)
            
          
    return lista