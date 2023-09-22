def busca(setor,matriz):
    1 = 0
    adicionar= []
    while 1< len(matriz):
        if setor in matriz:
            nome = matriz[i][0]
            registro = matriz[i][1]
            telefone = matriz[i][3]
            adicionar += [[nome,registro,telefone],]
        1 += 1
    return adicionar