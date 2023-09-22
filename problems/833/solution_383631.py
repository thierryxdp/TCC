def conta_numero(numero,matriz):
    
    contador=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                numero+=1
    return contador