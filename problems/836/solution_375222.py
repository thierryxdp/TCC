def busca(setor,matriz):
    resultado=[]
    for linha in range(len(matriz)):
        if setor==matriz[linha][2]:
            list.remove(matriz[linha],setor)
            list.append(resultado,matriz[linha])
    return resultado