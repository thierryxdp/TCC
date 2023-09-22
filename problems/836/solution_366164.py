def busca(setor,matriz):
    resultado=[]
    for c in range(len(matriz)):
        if setor==matriz[c][2]:
            resultado=resultado+[matriz[c]]
    return resultado