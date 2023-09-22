def busca(setor,matriz):
    funcionario=[]
    for n in range(len(matriz)):
        newcont=matriz[n]
        if setor in newcont[2]:
            funcionario=funcionario + [newcont]
            del(funcionario[2])
    return funcionario