def busca(setor,matriz):
    retorno = []
    for dado in matriz:
        for funcionario in dado:
            if funcionario == setor:
                retorno.append(dado)
    for item in retorno:
        for s in item:
            if s == setor:
                retorno = retorno[2].pop()
    return retorno