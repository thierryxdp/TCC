def busca (funcionarios,matriz):
    lista =[]
    for j in range(len(matriz)):
        if funcionarios == matriz[j][2]:
        lista = lista+[[matriz[j][0], matriz[j][1], matriz [j][3]]
		return lista