def melhor_volta(matriz):
    menor_tempo = min(matriz[0])
    tupla = (1,matriz[0].index(meno_tempo),menor_tempo)
    for i in matriz:
        if min(i) < menor_tempo:
            tupla = (matriz.index(i)+1,i.index(min(i))+1,min(i))
	return tupla