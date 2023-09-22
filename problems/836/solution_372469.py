def busca(setor,matriz):
    funcionario=[]
    for pessoa in range(len(matriz)):
        if setor in pessoa:
            funcionario.append(pessoa)
    return funcionario