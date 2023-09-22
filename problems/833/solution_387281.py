def conta_numero(numero,matriz):
    qtd_linhas=len(matriz)
    qtd_colunas=len(matriz[0])
    a=0
    b=0
    for i in matriz:
        if i == numero:
            a[i]=i.count(numero)+1
        for j in matriz:
            if j == numero:
                b[j]=j.count(numero)+1
    return  a+b