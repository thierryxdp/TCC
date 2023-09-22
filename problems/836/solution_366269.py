def busca(setor,matriz):
    contador=0
    retorno = []
    retorno2=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                contador=contador+1
                list.append(retorno,matriz[i])
    retorno3=[]
    for a in range(len(retorno)):
        linha=[]
        for b in range(len(retorno[a])):
            if retorno[a][b] != setor:
                list.append(linha,retorno[a][b])
        list.append(retorno3,linha)
                
         
    return retorno3