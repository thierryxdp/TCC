def busca(setor,matriz): 
    retorno=[]
    for i in range(len(matriz)):
        funcio=(matriz[i]) 
        lista=str.split(funcio)
        if setor in lista:
            list.append(retorno,matriz[i])
    return retorno