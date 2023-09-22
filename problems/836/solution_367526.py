def busca (setor, matriz):
    lista = []
    for j in range(len(matriz)):
        if setor == matriz[j][2]:
            lista += matriz[j] 
    return lista