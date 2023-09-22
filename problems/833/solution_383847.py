def conta_numero(numero,matriz):
    p=0
    for i in matriz:
        for k in i:
            if numero==k:
                p+=1
    return p