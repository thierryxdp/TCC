def media_matriz(matriz):
    soma=0
    qtd_ele=0
    for i in matriz:
        for j in i:
            soma=soma+int(j)
            qtd_ele=qtd_ele+1
    return round(soma/qtd_ele,2)