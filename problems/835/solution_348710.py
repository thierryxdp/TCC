def melhor_volta(matriz):
    volta=1000
    y=[]
    for a in matriz:
        for b in a:
            if b<volta:
                volta = b
	return volta