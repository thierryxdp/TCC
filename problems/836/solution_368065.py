def busca(setor,matriz):
    resultado=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            novalinha=matriz[i]
            del novalinha[2]
            resultado.append(novalinha)
    return resultado