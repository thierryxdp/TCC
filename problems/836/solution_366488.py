def busca (setor, lista):
    for a in range(len(lista)):
        if lista[a][2] == setor:
    		return list(lista[a][0] + ' ' + lista[a][1] + ' ' + lista[a][3])