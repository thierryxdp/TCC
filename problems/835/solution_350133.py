def melhor_volta(matriz):
    checagem = 999
    menor_volta = ()
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if matriz[contador][contagem] < checagem:
                menor_volta = (matriz[contador], checagem, matriz[contador][contagem])
	return menor_volta