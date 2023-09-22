def melhor_volta(matriz):
    tempo = 120
    volta = 0
    kart=0
    y=[]
    for a in matriz:
        for b in a:
            if b<tempo:
                tempo = b
                volta=a[b]
	return [tempo,volta]