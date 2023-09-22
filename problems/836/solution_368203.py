def busca(setor,lista):
    "Funcao que retorna lista de funcionarios de um setor"
    m=[]
    for i in range(len(setor)):
        n=[]
        for j in range(len(lista)):
            if lista[i][2] == setor:
                n.append(lista[i][0],lista[i][1],lista[i][3])
        		return n
    			else:
        			return '[]'