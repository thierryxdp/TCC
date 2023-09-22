def busca(setor,matriz):
    retorno = []
    for dado in matriz:
        for funcionario in dado:
            if funcionario == setor:
                retorno.append(dado)
    retorno[0][2].remove(setor)         
    
    return retorno