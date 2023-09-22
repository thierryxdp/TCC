def conta_numero(numero,matriz):
    c=0
    for lin in matriz:
        for col in lin:
            if numero==col:
                c=c+1
    return c