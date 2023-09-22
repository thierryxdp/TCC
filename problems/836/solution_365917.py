def busca(setor,matriz):
    retorno = []
    for funcionario in matriz:
        for dados in funcionario:
            if setor in dados:
                list.append(retorno,funcionario)
    return retorno