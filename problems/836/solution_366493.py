def busca (setor, lista):
    for a in range(len(lista)):
        if lista[a][2] == setor:
    		return lista[a].remove(lista[a][2])