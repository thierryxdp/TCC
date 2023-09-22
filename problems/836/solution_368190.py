def busca(setor,lista):
    "Funcao que retorna lista de funcionarios de um setor"
    n=[]
    for i in range(len(setor)):
        if lista[i][2] == setor:
            n.remove(lista[i][2])
            n.index(lista[i])
            return n