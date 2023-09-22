def melhor_volta(matriz):
    checagem = 99
    menor_volta = ()
    soma = 0
    for contador in range(len(matriz)):
        for contagem in range(len(matriz[contador])):
            if matriz[contador][contagem] < checagem:
                soma = soma + 1
                checagem = matriz[contador][contagem]
				menor_volta = (soma, checagem, matriz[contador][contagem])
	return menor_volta