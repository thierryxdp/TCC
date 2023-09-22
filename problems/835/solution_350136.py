def melhor_volta(matriz):
    checagem = 5
    menor_volta = ()
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if matriz[contador][contagem] < checagem:
                checagem = matriz[contador][contagem]
		menor_volta = (matriz[contador], checagem, matriz[contador][contagem])
	return menor_volta