def conta_numero(numero,matriz):
    n=0
    for linha in matriz:
        for elemento in linha:
        	if elemento == numero:
                n+=1
    return n