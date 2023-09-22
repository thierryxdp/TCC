def conta_numero(matriz, numero):
    count = 0
    for i in matriz:
        for n in i:
            if n==numero:
                count+=1
    return(count)