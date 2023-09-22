def busca(setor,lista):
    "Funcao que retorna lista de funcionarios de um setor"
    n=[]
    for i in range(len(setor)):
        if lista[i][2] == setor:
            n.pop(lista[i][2])
            n.append(lista[i])
            return n