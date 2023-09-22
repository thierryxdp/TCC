def conta_numero(numero, matriz):
    
    count = 0
    for i in matriz:
        for n in i:
            if n==numero:
                count+=1
    return(count)