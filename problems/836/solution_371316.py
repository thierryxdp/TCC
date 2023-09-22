def busca(setor:str, matriz:list[list])->list[list]:
    resultado = []
    for i in matriz:
        if i[2] == setor:
            resultado.append(i[0:2] + i[3:])
	return resultado