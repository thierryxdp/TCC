def busca(setor, matriz):
    resultado = []
    for linha in range(len(matriz)):
        for elemento in range(len(matriz[0])):
            if matriz[linha][elemento] == setor:
                list.append(resultado, (matriz[linha]))
        if (matriz[linha])[2] == setor:
            list.remove((matriz[linha]), setor)
    return resultado