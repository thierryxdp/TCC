def conta_numero(num, matriz):

    cont = 0

    for linha in matriz:
        for x in linha:
            if num == x:
                cont = cont + 1
        
    return cont