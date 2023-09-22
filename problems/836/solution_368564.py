def busca(setor,matriz):
    retorno = []
    for dado in matriz:
        for funcionario in dado:
            matriz.remove(setor)
            if funcionario == setor:
                retorno.append(dado)
    return retorno