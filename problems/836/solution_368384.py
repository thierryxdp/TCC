def busca(setor, matriz):
    workers = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            workers.append(
                matriz[i][:2]+matriz[i][3:]
            	)
    return workers

# Obs: 
#	1. A posição do setor na matriz é 2 e nao 1;
#	2. Você não pode usar o "return" onde usou
#	   pois isso cortar a possibilidade de encontrar
#	   mais nomes;
#	3. O que te interessao, segundo o exemplo, são
#	   os dados do funcionário exceto o setor, que
#	   quem buscou já sabe;