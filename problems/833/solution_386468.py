def conta(n,matriz):
    cont=0
    for i in matriz:
        for j in i:
            if j==n:
                cont= cont + 1
        return cont