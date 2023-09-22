def busca(setor,matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    funcionario = [] 
    total = []
    for i in nlin:
        if M[i][2] == setor:
            funcionario.append(M[i])
        total.append(funcionario)    
    return total