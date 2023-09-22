def melhor_volta(matriz):
i = 0
j = 0
menor = 0
	for i in range(0,6):
        for j in range(0,10):
            if matriz[j] == min(matriz):
                menor = matriz[j]
    i += 1
    j += 1
    return ("A melhor volta foi a do "+matriz[i]+"º corredor","o menor tempo foi "+matriz[j],"na volta "+matriz[j+1])