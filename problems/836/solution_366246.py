def busca(setor,matriz):
    contador=0
    retorno = []
    retorno2=[[]]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                contador=contador+1
                list.append(retorno,matriz[i])
    for a in range(len(retorno)):
        for b in range(len(retorno[a])):
            if retorno[a][b] != setor:
                list.append(retorno2[],retorno[a][b])
                
         
    return retorno2