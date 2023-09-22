def acima_da_media (lista: list[float]) -> list[float]:
    '''doc'''
    clista = lista.copy()
    clista.sort()

    #Fazendo a média das notas
    media = sum(clista)/len(clista)
    #Adicionando media a lista e ordenando 
    clista.append(media)
    clista.sort()
    #Pegando apenas as notas maiores
    p = clista.index(media)
    listaM = clista[p+1:]
    
    if n in listaM:
    	q = listaM.count(n)
        listaM = listaM[q:] 

    return listaM