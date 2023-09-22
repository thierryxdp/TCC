def busca (setor, matriz):
    lista = []
    for j in range(len(matriz)):
        if setor == matriz[j][2]:
            lista += [matriz[j][0],matriz[j][1],matriz[j][3]] 
    return lista