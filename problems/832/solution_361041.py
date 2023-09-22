def ah_quadrada(matriz):
    for i in matriz: 
        linha=i
        for j in matriz[i]:
            coluna=j 
            if coluna==linha: 
                return (True) 
            else:
                return (False)