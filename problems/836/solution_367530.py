def busca (setor, matriz):
    lista = []
    for linha in range(len(matriz)):
        if setor == matriz[linha][2]:
            lista.append([matriz[linha][0],matriz[linha][1],matriz[linha][3]]) 
    return lista