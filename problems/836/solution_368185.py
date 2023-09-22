def busca(setor,lista):
    "Funcao que retorna lista de funcionarios de um setor"
    n=[]
    for i in range(len(setor)):
        if lista[i][2] == setor:
            n.append(lista[i][0],lista[i][1],lista[i][3])
            return n