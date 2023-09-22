def busca(setor,matriz):
    funcionario=[]
    for n in range(len(matriz)):
        newcont=matriz[n]
        if setor in newcont[2]:
            funcionario=funcionario + [newcont]
            remov=funcionario[2]
        if remov in funcionario
        	list.remove(funcionario,remov)
    return funcionario