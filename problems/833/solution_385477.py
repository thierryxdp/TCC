def conta_numero(numero,matriz):
    c=0
    for x in matriz:
        for y in x:
            if y==numero:
                c+=1
	return c