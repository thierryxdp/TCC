def busca(setor,matriz):
    retorno = []
    for dado in matriz:
        for funcionario in dado:
            if funcionario == setor:
                retorno.append(dado)
    for item in retorno:
        for s in item:
            if s == setor:
                retorno = renorno[2].pop(2)
    return retorno