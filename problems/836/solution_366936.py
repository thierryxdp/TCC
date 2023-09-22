def busca(setor, matriz):
    
    saida = []
    for lista in matriz:
        temp = []
        if lista[2] == setor:
            temp = lista
            del temp[2]
            saida.append(temp)
    return saida