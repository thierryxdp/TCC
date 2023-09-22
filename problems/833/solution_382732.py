def conta_numero(numero,matriz):
    
    aparicoes=0

    for linha in matriz:
        for j in linha:
            if numero == j:
                aparicoes+=1

    return aparicoes