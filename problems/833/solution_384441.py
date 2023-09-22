def conta_numero(numero,matriz):
    contador=0
    for linha in matriz:
        for num in linha:
            if numero==num:
                contador+=1
	return contador