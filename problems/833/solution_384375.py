def conta_numero(numero,matriz):
    x=0
    for a in matriz:
        for b in a:
            if numero == b:
                x+=1
	return x