def busca(setor,lista):
    "Funcao que retorna lista de funcionarios de um setor"
    for i in range(len(setor)):
        n=[]
        for j in range(len(lista)):
            if lista[i][2] == setor:
                n.append(lista[i])
        		return n
            else:
        		return '[]'