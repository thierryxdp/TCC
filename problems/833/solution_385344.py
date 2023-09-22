def conta_numero(numero,matriz):
    ocorrencia=[]
    for i in matriz:
        for j in matriz:
            if matriz[i][j]==numero:
                q=q+1
        list.append(ocorrencia,q)
    return ocorrencia