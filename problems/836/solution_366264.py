def busca(setor,matriz):
    contador=0
    retorno = []
    retorno2=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                contador=contador+1
                list.append(retorno,matriz[i])
    
                
         
    return [matriz[0][0:3],matriz[0][3:],matriz[0][0:3],matriz[0][3:]]