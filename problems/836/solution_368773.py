def busca(setor,matriz):
    contato=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            contato=matriz[i]
            if setor not in matriz[i][2]:
                return []
    return contato