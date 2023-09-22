def busca(nome,matriz):
    
    contato = []
    for i in range(len(matriz)):
        if nome not in matriz[i][0]:
            contato = contato
        if nome in matriz[i][0]:
            contato = contato + matriz[i]
    return contato