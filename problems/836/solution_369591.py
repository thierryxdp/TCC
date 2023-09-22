def busca(setor,matriz):
    """A Funcao retorna os dados do funcionario de um determinado
	setor; str,list-->list"""
    funcionario=[]
    for n in range(len(matriz)):
        newcont=matriz[n]
        if setor in newcont[2]:
            funcionario=funcionario + [newcont]
            newcont.remove(setor)
    return funcionario