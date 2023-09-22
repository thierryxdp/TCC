def busca(string,matriz):
    
    vazia=[]
    
    for i in len(matriz):
        for j in len(matriz[i]):
            if matriz[i][j] in string:
                return matriz[i]