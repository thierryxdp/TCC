def busca(setor,matriz):
    funcionario=[]
    for n in range(len(matriz)):
        newcont=matriz[n]
        if telefone in newcont[1]:
            funcionario=funcionario + [newcont]
    return funcionario